import { v4 as uuidv4 } from 'uuid';


const state = {
    "anonymousId" : null,
}

const createAnonymousId = () => {
    if (state["anonymousId"] === null) {
        console.log('creating anon id')
        const newAnonymousId = uuidv4()
        console.log(newAnonymousId)
        data["anonymous_id"] = newAnonymousId
        localStorage.setItem("anonymousId", newAnonymousId)
    }
}



window.onload = function() {
    console.log("request");
    createAnonymousId()
    console.log('data', data)
    fetch('http://localhost:8000/pages/create/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
};

const data = {
    'anonymous_id': state["anonymousId"],
    'sent_at': new Date(),
    'user_agent': navigator.userAgent,
    'title': document.title,
    'path': window.location.pathname,
    'url': window.location.href,
    'referrer': document.referrer,
    'search': window.location.search,
}
