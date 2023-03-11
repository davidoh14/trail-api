import { v4 as uuidv4 } from 'uuid';


const createAnonymousId = () => {
    if (!localStorage["anonymousId"]) {
        const newAnonymousId = uuidv4()

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
    'anonymous_id': localStorage["anonymousId"],
    'sent_at': new Date(),
    'user_agent': navigator.userAgent,
    'title': document.title,
    'path': window.location.pathname,
    'url': window.location.href,
    'referrer': document.referrer,
    'search': window.location.search,
}
