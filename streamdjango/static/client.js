window.addEventListener("DOMContentLoaded", () =>{
    const websy = new WebSocket("ws://localhost:7568/");
    document.querySelector("#socket").addEventListener("click", () => {
        console.log("got in") 
        websy.send('give_data')
    });

    websy.onmessage = ({ data }) => {
        const json_data = JSON.parse(data)
        if ('ptbl' in json_data) {
            const tbl_data = json_data['ptbl']
            // console.log(tbl_data)
            document.querySelector("#socstreamer").innerHTML += `
            <div>
                <p><span>User Prompt: </span>${json_data['ptbl']['user_prompt']}</p>
                <p><span>LLM Reply: </span>${json_data['ptbl']['llm_reply']}</p>
            </div>
            `
            }
        }
});