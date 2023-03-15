import { v4 as uuidv4 } from 'uuid';


const getApiKeyFromScript = () => {
    const scriptSrc = document.getElementById('trail-api').getAttribute('src')
    const scriptSrcURL = new URL(scriptSrc)
    const scriptSearchParams = new URLSearchParams(scriptSrcURL.search)
    const apiKey = scriptSearchParams.get('apikey')

    return apiKey
}


const config = {
  baseURL: 'http://localhost:8000/pages/create/',
  headers: {
    'Content-Type': 'application/json',
    'X-Api-Key': getApiKeyFromScript(),
  }
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

const createAnonymousId = () => {
    if (!localStorage["trail_anon_id"]) {
        const newAnonymousId = uuidv4()

        localStorage.setItem("trail_anon_id", newAnonymousId)
        data["anonymous_id"] = newAnonymousId
    }
}

const pageEvent = async () => {
    console.log("request");
    createAnonymousId();
    console.log('data', data);
    console.log('auth', config.headers.Authorization)
    await fetch(config.baseURL, {
        method: 'POST',
        headers: config.headers,
        body: JSON.stringify(data)
    });
};


window.addEventListener('load', pageEvent);
