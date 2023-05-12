const add_to_cart = async (e) => {
    console.log(e)
    e.preventDefault();
    const url = e.target.getAttribute("href");
    console.log(url);

    const old_text = e.target.innerHTML;
    const response = await fetch(url + "?ajax=1");
    const data = await response.json();
    setTimeout(() => {
        e.target.innerHTML = old_text
    }, 1000);
    cart_count= document.getElementById("CartItemCount")
    cart_count.innerHTML = data.cart_count;
    cart_count.setAttribute("data-count", data.cart_count);
    closePopUp()
}




document.addEventListener('DOMContentLoaded', () => {
    cart_table = document.getElementById("CartTable")
    cart_quantity_fields = cart_table.querySelectorAll("input.quantity")
    add_to_cart_buttons = document.querySelectorAll(".add-to-cart")

    add_to_cart_buttons.forEach(button => {
        button.addEventListener('click', add_to_cart)
        console.log(button)
    });

    cart_quantity_fields.forEach(field => {
        console.log(field, field.getAttribute('data-cart-item'), field.value)
        field.addEventListener('change', async (e) => {
            let item_id = field.getAttribute('data-cart-item');
            let quantity = field.value;
            const url = (id, quantity) => `/cart/update/${id}/${quantity}?ajax=1`
            console.log("I'm here")
            e.target.disabled = true
            if (quantity <= 0) {
                if (confirm("Do you want to remove this item from your cart?")) {
                    await fetch(url(item_id, quantity));
                    window.location.reload()
                } else {
                    e.currentTarget.value = 1
                    await fetch(url(item_id, 1));
                }
            } else {
                let response = await fetch(url(item_id, quantity));
                let data = await response.json();
                console.log(data)
                let cart_item_row = cart_table.querySelector(`tr[data-cart-item="${item_id}"]`)
                let cart_item_total = cart_item_row.querySelector("td.item-total .value")
                let cart_total = cart_table.querySelector("td.cart-total .value")
                let cart_total_lp = cart_table.querySelector(".lp-earned")
                let cart_earned_lp = document.querySelectorAll(".lp-earned")
                let cart_spent_lp = cart_table.querySelector(".lp-spent")
                let cart_old_lp = cart_table.querySelector(".lp-old-balance")
                let cart_new_lp = cart_table.querySelector(".lp-new-balance")
                const numberWithCommas = (x) => {
                    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                }

                if (cart_item_total) {
                    cart_item_total.innerHTML = numberWithCommas(data.item_total_price)
                }
                if (cart_total) {
                    cart_total.innerHTML = numberWithCommas(data.total_price)
                }
                if (cart_total_lp) {
                    cart_total_lp.innerHTML = numberWithCommas(data.total_loyalty_points_price)
                }
                if (cart_earned_lp) {
                    cart_earned_lp.forEach(element => {
                        element.innerHTML = numberWithCommas(data.loyalty_points.earned)
                    });
                }
                if (cart_spent_lp) {
                    cart_spent_lp.innerHTML = numberWithCommas(data.loyalty_points.spent)
                }
                if (cart_old_lp) {
                    cart_old_lp.innerHTML = numberWithCommas(data.loyalty_points.old_balance)
                }
                if (cart_new_lp) {
                    cart_new_lp.innerHTML = numberWithCommas(data.loyalty_points.new_balance)
                }
            }
            console.log(e.currentTarget)
            e.target.disabled = false
        })
    });
});
