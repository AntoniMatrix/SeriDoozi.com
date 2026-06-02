
document.querySelectorAll('.faq-question').forEach(item => {
    item.addEventListener('click', () => {
        const answer = item.nextElementSibling;
        answer.style.display =
            answer.style.display === 'block' ? 'none' : 'block';
    });
});

document.addEventListener("scroll", () => {
    const supportBtn = document.getElementById("supportCall");
    const footer = document.getElementById("siteFooter");

    const footerTop = footer.getBoundingClientRect().top;
    const windowHeight = window.innerHeight;
    const offset = 50;

    if (footerTop + 80 < windowHeight + offset) {
        supportBtn.style.bottom =
            (windowHeight - footerTop + offset - 25) + "px";
    } else {
        supportBtn.style.bottom = offset + "px";
    }
});
