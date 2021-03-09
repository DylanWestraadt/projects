
const express = require('express');
const http = require('http');
const socketio = require('socket.io')
const messageFormat = require('../backend/utils/message')


//conect to mongo db used to run querts


let port = 3200
//initialize express
const app = express();
//create server 
const server =  http.createServer(app);
//open socket session in server 
const io = socketio(server,{
    cors: {
      origin: '*',
    }
  });

 
    
   
io.on('connection', (socket)=>{
   
    
    socket.on('disconnect',()=>{
        console.log("user disconnected");

    })
    socket.on("sendMessage", (username, userMessage)=>{
        const message =  messageFormat(username,userMessage);
        socket.emit('listen', message)
        console.log(message)
        
        
    });
})
server.listen(port, () => {
    console.log(`server is alive at http://localhost:${port}`);
});



