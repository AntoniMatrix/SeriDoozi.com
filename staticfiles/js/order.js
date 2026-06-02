console.log("✅ order.js loaded");

document.addEventListener("DOMContentLoaded", function () {

    const addItemBtn = document.getElementById("add-item-btn");
    const itemsContainer = document.getElementById("items-container");

    let itemIndex = 1; // ✅ چون آیتم اول در HTML هست

    const MAX_ITEMS = 3;

    // ✅ افزودن آیتم جدید
    addItemBtn.addEventListener("click", function () {

        if (itemIndex >= MAX_ITEMS) {
            alert("حداکثر می‌توانید ۳ آیتم به سفارش اضافه کنید.");
            return;
        }

        itemIndex++;

        const html = `
        <div class="order-item card p-3 mb-4" data-index="${itemIndex}">

            <div class="d-flex justify-content-between align-items-center mb-3">
                <strong>آیتم ${itemIndex}</strong>
                <button type="button" class="btn btn-sm btn-danger remove-item-btn">
                    <i class="bi bi-trash"></i>
                </button>
            </div>

            <label>نوع محصول</label>
            <input type="text" class="form-control mb-3"
                name="items[${itemIndex}][title]" required>

            <label>نوع سفارش</label>
            <select class="form-select order-type mb-3"
                name="items[${itemIndex}][size_mode]" required>
                <option value="">انتخاب کنید</option>
                <option value="NORMAL">عادی</option>
                <option value="VIP">VIP</option>
            </select>

            <!-- ✅ NORMAL -->
            <div class="normal-section mb-3" style="display:none">
                <label>تعداد کل</label>
                <input type="number" class="form-control mb-2"
                    name="items[${itemIndex}][quantity]" min="1">

                <label>سایزبندی</label>
                <div class="d-flex gap-2">
                    <input type="text" class="form-control"
                        name="items[${itemIndex}][size_from]" placeholder="از">
                    <input type="text" class="form-control"
                        name="items[${itemIndex}][size_to]" placeholder="تا">
                </div>
            </div>

            <!-- ✅ VIP -->
            <div class="vip-section mb-3" style="display:none">
                <button type="button"
                    class="btn btn-outline-primary btn-sm mb-2 add-size-btn">
                    افزودن سایز
                </button>
                <div class="vip-sizes"></div>
            </div>

            <label>نوع پارچه</label>
            <input type="text" class="form-control mb-3"
                name="items[${itemIndex}][fabric_type]">

            <label>توضیحات</label>
            <textarea class="form-control mb-3"
                name="items[${itemIndex}][description]"></textarea>

            <label>عکس نمونه کار</label>
            <input type="file" class="form-control"
                name="items[${itemIndex}][sample_image]" accept="image/*">

        </div>
        `;

        itemsContainer.insertAdjacentHTML("beforeend", html);

        if (itemIndex >= MAX_ITEMS) {
            addItemBtn.disabled = true;
        }
    });

    // ✅ حذف آیتم
    document.addEventListener("click", function (e) {
        if (e.target.closest(".remove-item-btn")) {
            e.target.closest(".order-item").remove();
        }
    });

    // ✅ تغییر NORMAL / VIP
    document.addEventListener("change", function (e) {
        if (!e.target.classList.contains("order-type")) return;

        const item = e.target.closest(".order-item");

        const normalSection = item.querySelector(".normal-section");
        const vipSection = item.querySelector(".vip-section");
        const quantityInput = item.querySelector(".quantity-input");

        if (e.target.value === "NORMAL") {
            // ✅ NORMAL MODE
            normalSection.style.display = "block";
            vipSection.style.display = "none";

            quantityInput.required = true;
            quantityInput.disabled = false;

        } else {
            // ✅ VIP MODE
            normalSection.style.display = "none";
            vipSection.style.display = "block";

            quantityInput.required = false;
            quantityInput.disabled = true;
            quantityInput.value = ""; // جلوگیری از ارسال مقدار اشتباه
        }
    });


    // ✅ افزودن سایز VIP
    document.addEventListener("click", function (e) {
        if (e.target.closest(".add-size-btn")) {

            const item = e.target.closest(".order-item");
            const container = item.querySelector(".vip-sizes");
            const idx = item.dataset.index;
            const count = container.children.length;

            if (count >= 16) {
                alert("حداکثر ۱۶ سایز مجاز است");
                return;
            }

            const row = `
            <div class="row g-2 mb-2 vip-size-row">
                <div class="col-6">
                    <input type="text" class="form-control"
                        name="items[${idx}][vip_sizes][${count}][size]"
                        placeholder="سایز" required>
                </div>
                <div class="col-4">
                    <input type="number" class="form-control"
                        name="items[${idx}][vip_sizes][${count}][quantity]"
                        placeholder="تعداد" min="1" required>
                </div>
                <div class="col-2">
                    <button type="button"
                        class="btn btn-sm btn-outline-danger remove-size-btn">×</button>
                </div>
            </div>
            `;

            container.insertAdjacentHTML("beforeend", row);
        }
    });

    // ✅ حذف سایز VIP
    document.addEventListener("click", function (e) {
        if (e.target.closest(".remove-size-btn")) {
            e.target.closest(".vip-size-row").remove();
        }
    });

});


// ✅ جلوگیری از ثبت VIP بدون سایز
document.getElementById("orderForm").addEventListener("submit", function (e) {

    let hasError = false;

    document.querySelectorAll(".order-item").forEach(item => {
        const type = item.querySelector(".order-type")?.value;

        if (type === "VIP") {
            const sizes = item.querySelectorAll(".vip-size-row");
            if (sizes.length === 0) {
                alert("برای سفارش VIP حداقل یک سایز وارد کنید");
                hasError = true;
            }
        }
    });

    if (hasError) e.preventDefault();
});
