// Add click handlers to product cards to show a popup
const product_card_links = document.querySelectorAll(".product-list .card a");
const product_popup = document.getElementById("Popup");
const product_popup_content = product_popup.querySelector(".content");



closePopUp = () => {
    document.body.classList.remove("overlay");
}

product_card_links.forEach(link => {
    link.addEventListener('click', async (e) => {
        e.preventDefault();
        const url = e.currentTarget.getAttribute("href");
        console.log(url);

        const response = await fetch(url + "?ajax=1");
        const popup_content = await response.text();
        product_popup_content.innerHTML = popup_content;
        document.body.classList.add("overlay");

        // Get the #OfferInstance form
        const offer_form = document.getElementById("OfferInstance");
        offer_form.addEventListener('submit', async (e) => {
            e.preventDefault()
            const url = e.currentTarget.getAttribute("action")+ "?ajax=1";
            const formData = new FormData(e.currentTarget);
            const response = await fetch(url, {
                method: 'POST',
                body: formData,
            });
            const data = await response.json();
            console.log(data);
            // TODO: show that cart has been updated
            cart_count= document.getElementById("CartItemCount")
            cart_count.innerHTML = data.cart_count;
            cart_count.setAttribute("data-count", data.cart_count);
            closePopUp();
        });
    })
});



$(document).ready(function(){

    $('#search-form').on('submit', function(e) {

        e.preventDefault();
        let searchText = $('#search_filter').val();

        $.ajax({
            url: '?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                console.log(resp.data.map)
        let  newHtml= resp.data.map(d => (
          `<div class="card"> <a href ="products/${d.id}/ "><img class="thumb" src="/media/${d.picture}" alt="${d.name}"><div class="label"><a href="/products/${d.id}"> ${d.name} </a> <p>${d.description}</p></div></a></div>`
        ))
        $('.product-list').html(newHtml.join(''));
        console.log(newHtml,resp.data)
        $('#search-box').val('');
            },
            error: function (xhr, status, error) {
                //TODO: make better
                console.error(error);
            }
        })
    });
});

openCategory = (name) => {
  var i;
  var x = document.getElementsByClassName("city");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  document.getElementById(cityName).style.display = "block";
}







// <div className="card">
//     <a href="{% url 'product_details' product.id %}">
//         <img className="thumb" src="{{  product.picture.url }}" alt="{{ product.name }}">
//             <div className="label">
//                 <a href="{% url 'product_details' product.id %}">{{product.name}}</a>
//                 <p>{{product.description}}</p>
//             </div>
//     </a>
// </div>
