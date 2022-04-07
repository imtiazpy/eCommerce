const updateBtns = document.getElementsByClassName("update-cart");

for (const btn of updateBtns) {
    btn.addEventListener("click", function () {
        const productId = this.dataset.product;
        const action = this.dataset.action;

        if (user === 'AnonymousUser') {
            console.log("User not logged in")
        } else {
            console.log("User is valid, sending data")
        }
    })
};

