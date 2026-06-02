let rowIndex = 1;

// ── افزودن ردیف جدید ──
document.getElementById('add-item').addEventListener('click', () => {
    const tbody = document.getElementById('items-body');
    const row = document.createElement('tr');
    row.style = 'width: 100%';
    row.className= 'item-row-value en-font'
    row.innerHTML = `
        <td style="width: 10%">
        <input type="text" name="items-${rowIndex}-title" class="form-control form-control-sm"
                placeholder="عنوان آیتم" required maxlength="255">
        </td>
        <td style="width:70%">
        <input type="text" name="items-${rowIndex}-description" class="form-control form-control-sm"
                placeholder="توضیحات (اختیاری)">
        </td>
        <td style="width:5%">
        <input type="number" name="items-${rowIndex}-quantity" class="form-control form-control-sm qty"
                value="1" min="1" required>
        </td>
        <td style="width:5%">
        <input type="text" name="items-${rowIndex}-unit" class="form-control form-control-sm"
                value="عدد" maxlength="50">
        </td>
        <td style="width:7%">
        <input type="number" name="items-${rowIndex}-unit_price_amount"
                class="form-control form-control-sm price" min="0" required>
        </td>
        <td class="text-center" style="width:3%">
        <button type="button" class="btn btn-sm btn-outline-danger remove-row">
            <i class="bi bi-trash"></i>
        </button>
        </td>
                    `;
    tbody.appendChild(row);
    rowIndex++;
    document.getElementById('id_items-TOTAL_FORMS').value = rowIndex;
    
    recalc();
});

// ── محاسبه جمع ──
function recalc() {
    let subtotal = 0;
    document.querySelectorAll('.item-row-value').forEach(row => {
        const qty   = parseFloat(row.querySelector('.qty')?.value)   || 0;
        const price = parseFloat(row.querySelector('.price')?.value) || 0;
        subtotal += qty * price;
    });
    const taxRate = parseFloat(document.getElementById('id_tax_rate').value) || 0;
    const tax     = (subtotal * taxRate) / 100;
    const total   = subtotal + tax;

    const fmt = n => n.toLocaleString('fa-IR') + ' ریال';
    document.getElementById('summary-subtotal').textContent = fmt(subtotal);
    document.getElementById('summary-tax').textContent      = fmt(tax);
    document.getElementById('summary-total').textContent    = fmt(total);
    document.getElementById('summary-tax-rate').textContent = taxRate;
}

// ── init ──
document.getElementById('id_tax_rate').addEventListener('input', recalc);

recalc();

  // جای bindEvents برای remove-row، این رو بذار روی tbody
document.getElementById('items-body').addEventListener('click', (e) => {
  const btn = e.target.closest('.remove-row');
  
  if (!btn) return;
  if (document.querySelectorAll('.item-row-value').length > 1) {

    btn.closest('tr').remove();
    recalc();
  }
});

document.getElementById('items-body').addEventListener('input', (e) => {
    
    if (e.target.matches('.qty, .price')) {
        recalc();
    }
});

jalaliDatepicker.startWatch({theme: 'dark'});

