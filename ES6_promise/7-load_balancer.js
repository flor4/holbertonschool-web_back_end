export default function loadBalancer(chinaDownload, UsDownload) {
    return Promise.any([chinaDownload, USDownload]).then((value) => {return value});
}
