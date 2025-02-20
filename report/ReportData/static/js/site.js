$(document).ready(function () {
    $.getJSON("/reportapi/", function (data) {
        $("#date").text(data.date);
        $("#report_no").text(data.daily_report_no);
        $("#page").text(data.page);

        data.pictures.forEach(pic => {
            $('#picture_info').append(`
                <div class="photo-container">
                    <img src="/static/images/${pic.file_name}" alt="${pic.description}" style="width: 280px;">
                </div>
                <table class="table">
                    <tr>
                        <td><b>Location:</b> ${pic.location}</td>
                    </tr>
                    <tr>
                        <td><b>Description:</b> ${pic.description}</td>
                    </tr>
                </table>
            `);
        });
    });
});
