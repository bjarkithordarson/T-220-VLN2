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

        const response = await fetch(url + "?popup=1");
        const popup_content = await response.text();
        product_popup_content.innerHTML = popup_content;
        document.body.classList.add("overlay");
        console.log(popup_content);
        //window.history.pushState('page2', 'Title', url);
    })
});

$(document).ready(function(){
    $('#search-form').on('submit', function(e) {

        e.preventDefault();
        let searchText = $('#search_box').val();

        $.ajax({
            url: '?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
        let  newHtml= resp.data.map(d => (
          `<div class="card"> <a href ="products/${d.id}/ "><img class="thumb" src="/media/${d.picture}" alt="${d.name}"><div class="label"><a href="/products/${d.id}"> ${d.name} </a> <p>${d.description}</p></div></a></div>`)
        )

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

// <div className="card">
//     <a href="{% url 'product_details' product.id %}">
//         <img className="thumb" src="{{  product.picture.url }}" alt="{{ product.name }}">
//             <div className="label">
//                 <a href="{% url 'product_details' product.id %}">{{product.name}}</a>
//                 <p>{{product.description}}</p>
//             </div>
//     </a>
// </div>
