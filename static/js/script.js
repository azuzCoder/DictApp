function changeDisplayCreateForm(displayType) {
    form = document.getElementById('create-form')
    form.style.display = displayType;
}
function changeCreateButton(displayType) {
    button = document.getElementById('create-button')
    button.style.display = displayType;
}

function onClickCreateButton() {
    changeCreateButton("none")
    changeDisplayCreateForm("inline-block")
}

function cancelCreateForm() {
    changeDisplayCreateForm("none")
    changeCreateButton("inline-block")
}