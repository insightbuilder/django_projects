from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from faker import Faker
from faker_food import FoodProvider
from .models import Customer, Purchase, questions
import logging
import random
logging.basicConfig(format='%(message)s|%(asctime)s',
                    datefmt='%d-%m-%y:%H-%M-%S',
                    level=logging.INFO,)
from datetime import datetime
from jinja2 import (
    Environment,
    select_autoescape,
    FileSystemLoader,
    meta
)
import os
from openai import OpenAI
from dotenv import load_dotenv
from django.http import StreamingHttpResponse
import time

env_template = Environment(
    loader=FileSystemLoader('D:\\streamdjango\\shop\\jinja_prompt'),
    autoescape=select_autoescape
)

# open_ai details
model_used_eco = "gpt-3.5-turbo"
sql_data_analyst = "You are expert in SQL, data analysis and munging huge volumes of data. You can think about the given question step by step and answer in single line."
load_dotenv("D:\\streamdjango\\shop\\.env")

def llm_call_openai(user_message: str,
                    system_message: str,
                    model_used: str):
    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    try:
        response = client.chat.completions.create(
            model=model_used,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "system", "content": user_message}
            ],
            temperature=0.0,
            top_p=1,
            frequency_penalty=0.1,
            presence_penalty=0.1,
        )
        assistant_message = response.choices[0].message.content
        logging.info(f"Tokens used: {response.usage.total_tokens}")
        return {"response": assistant_message}
    except Exception as e:
        logging.info(e)
        return {"error": "An error occurred while processing the request."}

def index_home(request):
    return render(request, 'index.html', {"test": "test"})


def page404(request):
    return render(request, 'page404.html', {'err':'err'})


def get_new_name(request):
    # show the data as table on front end
    faker = Faker()
    user_data = [
        dict(name=faker.name(),
             card=faker.credit_card_number())
        for _ in range(1)
    ]
    context = {"userdata": user_data}
    return render(request, 'index.html', context)


def show_name(request):
    customer_list = []
    cobjs = Customer.objects.all()
    for cdata in cobjs:
        logging.info(cdata.pk)
        customer_list.append({
            "name": cdata.name,
            "card": cdata.card
        })
    return render(request, 'index.html', {'userdb': customer_list})


def push_name(request, name, card):
    name_obj = {"name": name, "card": card}
    customer = Customer(**name_obj)
    try:
        customer.save()
    except Exception as e:
        logging.info(e)
        return redirect('page404')

    customer_list = []
    cobjs = Customer.objects.all()
    for cdata in cobjs:
        customer_list.append({
            "name": cdata.name,
            "card": cdata.card
        })
    return render(request, 'index.html', {'userdb': customer_list})


def del_names(request):
    cobj = Customer.objects.all().delete()
    context = {"status": "Names Deleted"}
    return render(request, 'index.html', context)


def get_new_item(request):
    # show the data as table on front end
    faker = Faker()
    faker.add_provider(FoodProvider)
    print(faker.dish())
    # select a customer
    objs = Customer.objects.all()
    customer_len = len(objs)
    rand_customer = random.randint(0, customer_len - 1)
    logging.info(rand_customer)
    customer = objs[rand_customer] 
    item_data = []
    
    for _ in range(1):
        price = random.randint(10, 25)
        quantity = random.randint(2, 7)
        total_spend = price * quantity

        item_data.append(dict(name=customer.name,
                              item_purchase=faker.dish(),
                              price=price,
                              quantity=quantity,
                              total_spend=total_spend,
                              purchase_ts=datetime.now()
                              )
        )
    context = {"itemdata": item_data}
    return render(request, 'index.html', context)


def show_item(request):
    items_list = []
    pobjs = Purchase.objects.all()
    for pdata in pobjs:
        items_list.append({
            "name": pdata.name.name,
            "item": pdata.item_purchase,
            "quantity": pdata.quantity,
            "price": pdata.price,
            "total_spend": pdata.total_spend,
            "purchase_ts": pdata.purchase_ts
        })
    return render(request, 'index.html', {'itemsdb': items_list})


def push_item(request, name, item, price, qty, spend, ts):
    customer = get_object_or_404(Customer, name=name)
    item_dict = dict(name=customer,
                     item_purchase=item,
                     price=price,
                     quantity=qty,
                     total_spend=spend,
                     purchase_ts=ts
                    )
    txn = Purchase(**item_dict)
    try:
        txn.save()
    except Exception as e:
        logging.info(e)
        return redirect('page404')

    item_list = []
    pobjs = Purchase.objects.all()
    for pdata in pobjs:
        item_list.append(dict(name=pdata.name.name,
                              item=pdata.item_purchase,
                              price=pdata.price,
                              quantity=pdata.quantity,
                              total_spend=pdata.total_spend,
                              purchase_ts=pdata.purchase_ts
                              )
        )
    return render(request, 'index.html', {'itemsdb': item_list})


def del_items(request):
    pobj = Purchase.objects.all().delete()
    context = {"item_status": "Items Deleted"}
    return render(request, 'index.html', context)


def get_llm(request):
    sql_temp = env_template.get_template("sql_analysis.prompt")
    items_list = []
    pobjs = Purchase.objects.all()
    for pdata in pobjs:
        items_list.append({
            "name": pdata.name.name,
            "item": pdata.item_purchase,
            "quantity": pdata.quantity,
            "price": pdata.price,
            "total_spend": pdata.total_spend,
            "purchase_ts": pdata.purchase_ts
        })
 
    if request.GET:
        text_query = request.GET['text_query']
        sql_analysis = sql_temp.render(question=text_query,
                                       itemsdb=items_list)
        reply_llm = llm_call_openai(user_message=sql_analysis,
                                    system_message=sql_data_analyst,
                                    model_used=model_used_eco)['response']
        logging.info(reply_llm)
        qobj = questions(question=text_query,
                         prompt=sql_analysis,
                         answer=reply_llm) 
        qobj.save()
        return render(request, 'index.html', {'prompt': sql_analysis, 
                                              'reply': reply_llm})
    reply_llm = 'There was error' 
    sql_analysis = 'get request failed'
    text_query = 'Query did not reach server'
    qobj = questions(question=text_query,
                         prompt=sql_analysis,
                         answer=reply_llm) 
    qobj.save()
    return render('page404')


def stream_reply(request):
    qobjs = questions.objects.all()
    prompt_reply = "" 
    for qobj in qobjs: 
        prompt_reply += f"""Question is: <br> {qobj.question} <br> Answer is: <br> {qobj.answer} <br>"""
    def gen_reply(prompt_reply):
        logging.info(prompt_reply)
        chunked_reply = prompt_reply.split(' ')
        for ind in range(len(chunked_reply)):
            time.sleep(0.5)
            yield chunked_reply[ind] + " "
    response = StreamingHttpResponse(gen_reply(prompt_reply),
                                    content_type='text/plain')
    return response


def show_questions(request):
    questions_list = []
    qobjs = questions.objects.all()
    for pdata in qobjs:
        questions_list.append({
            "question": pdata.question,
            "prompt": pdata.prompt,
            "answer": pdata.answer,
        })
    return render(request, 'index.html', {'questdb': questions_list})

def del_questions(request):
    qobjs = questions.objects.all().delete()
    return render(request, 'index.html', {'qstatus': 'deleted'})
