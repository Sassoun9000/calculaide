function suivantBtn() {
    document.getElementById("form_nav").style.border = "10px solid red";
}

document.getElementById("id_family_members_0").addEventListener("click", update())

document.getElementsByClassName("previous").addEventListener("load", suivantBtn())

console.log("coucou")