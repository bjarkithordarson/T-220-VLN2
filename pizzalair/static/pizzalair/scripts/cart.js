const add_to_cart = async (e) => {
    console.log(e)
    e.preventDefault();
    const url = e.target.getAttribute("href");
    console.log(url);

    const old_text = e.target.innerHTML;
    e.target.innerHTML = "Adding to cart..."
    const response = await fetch(url + "?ajax=1");
    const data = await response.json();
    e.target.innerHTML = "Done!"
    setTimeout(() => {
        e.target.innerHTML = old_text
    }, 1000);
    cart_count= document.getElementById("CartItemCount")
    cart_count.innerHTML = data.cart_count;
    cart_count.setAttribute("data-count", data.cart_count);
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

                let cart_item_row = cart_table.querySelector(`tr[data-cart-item="${item_id}"]`)
                let cart_item_total = cart_item_row.querySelector("td.item-total")
                let cart_total = cart_table.querySelector("td.cart-total")
                console.log(cart_item_row, cart_item_total, cart_total)
                const numberWithCommas = (x) => {
                    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                }

                cart_item_total.innerHTML = numberWithCommas(data.item_total_price) + " kr."
                cart_total.innerHTML = numberWithCommas(data.total_price) + " kr."
            }
            console.log(e.currentTarget)
            e.target.disabled = false
        })
    });
});
