"use strict";

function sendRequest() {
    $.ajax({
        method: 'GET',
        url: '/requests',
        mimeType: 'application.json',
        dataType: 'json',
        success: (data, status) => {
            console.log(data);
        }
    })
}

setInterval(sendRequest, 1000);