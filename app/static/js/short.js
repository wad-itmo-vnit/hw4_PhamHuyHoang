let http = new XMLHttpRequest();
const url = 'shortPolling/chat';
let form = document.querySelector('#user-chat');
let  dialog = document.querySelector("#dialog");

function addChat(user, message){
    let chat = `<p><b>${user}: </b>${message}</p>`;
    dialog.innerHTML+= chat;
}

http.onreadystatechange = () =>{
    if(http.readyState==4 && http.status==200){
        let res = JSON.parse(http.responseText);
        addChat(res.user,res.message);
    }  
};

formData = new FormData(form);

form.onsubmit =(e)=>{
    e.preventDefault();
    formData.set('user',document.querySelector("#user").value);
    formData.set('message',document.querySelector("#message").value);
    if(formData.get('user') != '' && formData.get('message')!=''){
        addChat(formData.get('user'),formData.get('message'));
        document.querySelector("#message").value='';
    };
    http.open('POST','/chat');
    http.send(formData);
};


function sendRequest (){
    http.open('POST',url);
    http.send();
}

setInterval(sendRequest,1000)