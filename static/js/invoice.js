document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("print");
    if (btn) {
        btn.addEventListener("click", function () {
            window.print();
        });
    }
});