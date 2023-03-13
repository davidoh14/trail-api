import { v4 as uuidv4 } from 'uuid';


const createAnonymousId = () => {
    if (!localStorage["trail_anon_id"]) {
        const newAnonymousId = uuidv4()

        localStorage.setItem("trail_anon_id", newAnonymousId)
        data["anonymous_id"] = newAnonymousId
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
    'anonymous_id': localStorage["trail_anon_id"],
    'sent_at': new Date(),
    'user_agent': navigator.userAgent,
    'title': document.title,
    'path': window.location.pathname,
    'url': window.location.href,
    'referrer': document.referrer,
    'search': window.location.search,
}
