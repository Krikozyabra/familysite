window.onload = function () {
    let searcher = document.forms[0].keywords

    searcher.addEventListener("input", () => {
        fetch(`http://localhost:8000/updateData?keywords=${searcher.value}`)
            .then(response => response.json())
            .then(res => drawList(res))
    })

}

function drawList(members) {
    let parent = document.getElementById("members")
    parent.innerHTML = '';
    for(let i = 0; i<members['mens'].length; i++){
        let memP = document.createElement('p')
        let memA = document.createElement('a')
        memA.innerHTML = members['mens'][i]['name']
        memA.classList.add("man")
        memA.href = members['mens'][i]['url']
        if(i === 0) memP.classList.add('first')
        if(i === members['mens'].length-1) memP.classList.add("last")
        memP.appendChild(memA)
        parent.appendChild(memP)
        console.log(memP)
    }
}

function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}