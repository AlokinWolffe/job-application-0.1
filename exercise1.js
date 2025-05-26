let offline = document.getElementsByClassName("offline");
let online = document.getElementsByClassName("online");

let all = document.getElementById('all');
let off = document.getElementById('off');
let on = document.getElementById('on');

function show_func(offline_val, online_val) {
    Array.from(offline).forEach(function (element) {
        element.style.display = offline_val;
    });

    Array.from(online).forEach(function (element) {
        element.style.display = online_val;
    });
}

function show_all() {
    show_func("block","block")
}

function show_off() {
    show_func("block","none")
}

function show_on() {
    show_func("none","block")
}

all.addEventListener('click', show_all);
off.addEventListener('click', show_off);
on.addEventListener('click', show_on);