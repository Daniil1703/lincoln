function ajaxPagination()
{
    $('#pagination a.page-link').each((index, el) =>{
        $(el).click((e) => {
            e.preventDefault()
            let page_url = $(el).attr('href')
            console.log(page_url)

            $.ajax({
                url: page_url,
                type: 'GET',
                success: (data) => {

                    $('.do_it').append( $(data).filter('.do_it').html())

                    $('.pagination').empty()

                    $('.pagination').append( $(data).find('.pagination').html())
                }
            })
        })
    })
}

$(document).ready(function() {
    ajaxPagination()
})

$(document).ajaxStop(function() {
    ajaxPagination()
})