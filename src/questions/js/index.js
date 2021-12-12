aides = {
    "1": ["14879", "19074", "29148", ">29148"],
    "2": ["21760", "27896", "42848", ">42848"],
    "3": ["26170", "33547", "51592", ">51592"],
    "4": ["30572", "39192", "60336", ">60336"],
    "5": ["34993", "44860", "69081", ">69081"],
    "6": ["39405", "50511", "77825", ">77825"],
    "7": ["43817", "56162", "86569", ">86569"],
    "8": ["48229", "61813", "95313", ">95313"],
  }

  function suivantBtn() {
      document.getElementById("form_nav").style.border = "10px solid red";
  }

  document.getElementById("id_family_members_0").addEventListener("click", update())

  document.getElementsByClassName("previous").addEventListener("load", suivantBtn())