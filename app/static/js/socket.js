const socket = io ();
let form = document.querySelector('#user-chat');
let  dialog = document.querySelector("#dialog");

function addChat(user, message){
    let chat = `<p><b>${user}: </b>${message}</p>`;
    dialog.innerHTML+= chat;
}

socket.on('connect',() => {
    console.log('connected');
})

socket.on('message', (data) => {
    addChat(data.user,data.message);
})


form.onsubmit =(e)=>{
    e.preventDefault();
    let user = document.querySelector("#user").value;
    let message = document.querySelector("#message").value;
    let data = {
        'user' : user,
        'message' : message
    }

    if(user != '' && message !=''){
        addChat(user,message);
        document.querySelector("#message").value='';
        socket.send(data);                 
    };
};

function sendAuto(){
    socket.emit('sendAuto');
}
setInterval(sendAuto,10000);     