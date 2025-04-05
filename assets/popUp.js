function createModal() {
    const popUp = document.createElement("div")
    popUp.innerHTML = `
        <!-- The button to open modal -->
        <label for="my_modal_7" id="button_pop_up" class="hidden">open modal</label>

        <!-- Put this part before </body> tag -->
        <input type="checkbox" id="my_modal_7" class="modal-toggle" />
        <div class="modal" role="dialog">
        <div class="modal-box">
            <h3 class="text-lg font-bold">In Development!</h3>
            <p class="py-4">New feature currently under development</p>
        </div>
        <label class="modal-backdrop" for="my_modal_7">Close</label>
        </div>`
    return popUp
}
document.body.append(createModal())

function actionButton() {
    const button = document.getElementById("button_pop_up")
    button.click()
}