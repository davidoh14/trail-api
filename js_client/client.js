const currentUrl = window.location.href
const requestSendTime = new Date()

data = {
    'session_id': '1',
    'session_creation_time': requestSendTime,
    'received_at': requestSendTime,
    'sent_at': requestSendTime,
    'ip': '192.158.1.38',
    'browser': 'Brave',
    'os': 'Mac OS X',
    'title': 'title',
    'path': '/path/',
    'url': 'http://www.url.com',
    'referrer': 'http://www.referrer.com',
    'search': '?search=search',
}

window.onload = function() {
    console.log("1");
    // Do something here, like manipulate the HTML elements
    fetch('http://localhost:8000/pages/create/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
};

