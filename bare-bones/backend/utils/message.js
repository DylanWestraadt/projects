const moment = require('moment');

const messageFormat = (username, message) =>{
   
    const format = {
        time: moment().format('h:mm a'),
        username: username,
        message: message
    };
    return format;
}
//use module.exports for node 
module.exports = messageFormat;