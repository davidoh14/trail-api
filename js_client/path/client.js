const requestSendTime = new Date()

const data = {
    'session_id': '1',
    'session_creation_time': requestSendTime,
    'sent_at': requestSendTime,
    'user_agent': navigator.userAgent,
    'title': document.title,
    'path': window.location.pathname,
    'url': window.location.href,
    'referrer': document.referrer,
    'search': window.location.search,
}

window.onload = function() {
    console.log("1");
    fetch('http://localhost:8000/pages/create/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
};

