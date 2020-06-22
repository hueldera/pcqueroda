var selectedNameList = {};

function addSelectedClass() {
  var allItems = document.querySelectorAll(".image-list li");
  for (var i = 0; i < allItems.length; i++) {
    var itemId = $(allItems[i]).data("id");
    if (selectedNameList[itemId]) {
      allItems[i].classList.add("selected-item");
    }
  }
}

function updateResultsLink() {
  $(".next-button").attr(
    "href",
    "results?sw=" + Object.keys(selectedNameList).join("&sw=")
  );
}

function UpdatedSelectedItems() {
  addSelectedClass();
  var selectedItems = document.querySelectorAll(".image-list .selected-item");
  var textToUpdate = document.querySelector("#selected-items-text");
  var buttonToDisable = document.querySelector(".next-button");

  for (var i = 0; i < selectedItems.length; i++) {
    var itemId = $(selectedItems[i]).data("id");
    var itemText = $(selectedItems[i]).find("h3").text();
    if (!selectedNameList[itemId]) {
      selectedNameList[itemId] = itemText;
    }
  }

  if (Object.keys(selectedNameList).length <= 0) {
    textToUpdate.innerText = "Selecione algum software ou jogo para continuar.";
    buttonToDisable.classList.add("disabled-button");
  } else {
    textToUpdate.innerText = `Você selecionou: ${Object.values(
      selectedNameList
    )}`;
    buttonToDisable.classList.remove("disabled-button");
  }

  updateResultsLink();
}

function addEventClickToItems() {
  function toggleSelectItemClass(e) {
    e.target.classList.toggle("selected-item");
    var itemId = $(e.target).data("id");
    if (selectedNameList[itemId]) {
      delete selectedNameList[itemId];
    }
  }
  var searchListItems = document.querySelectorAll(".image-list li");

  for (var i = 0; i < searchListItems.length; i++) {
    searchListItems[i].addEventListener("click", (e) => {
      toggleSelectItemClass(e);
      UpdatedSelectedItems();
    });
  }
  UpdatedSelectedItems();

  console.log("added");
}

addEventClickToItems();
