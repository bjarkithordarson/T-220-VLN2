// Add click handlers to product cards to show a popup
const product_card_links = document.querySelectorAll(".product-list .card a");
const product_popup = document.getElementById("Popup");
const product_popup_content = product_popup.querySelector(".content")
product_card_links.forEach(link => {
    link.addEventListener('click', async (e) => {
        e.preventDefault();
        const url = e.currentTarget.getAttribute("href");
        console.log(url);

        const response = await fetch(url + "?popup=1");
        const popup_content = await response.text();
        product_popup_content.innerHTML = popup_content;
        document.body.classList.add("overlay");
        console.log(popup_content);
        window.history.pushState('page2', 'Title', url);
    })
});
