const categoryServices = {
    "فيديو وأنيميشن": ["مونتاج فيديو", "ترجمة فيديو", "تصميم انترو", "تحريك شخصيات", "تحريك شعار", "موشن جرافيك",
        "تصميم صور GIF", "رسوم متحركة للأطفال", "تصميم فيديوهات تعليمية", "تسجيل الشاشة", "وايت بورد",
        "فيديوهات سوشيال ميديا", "تصميم فيديو إعلاني", "تصميم سلايد شو", "دعوة زواج", "أعياد ومناسبات"],

    "تصميم": ["منشورات سوشيال ميديا", "إعلانات سوشيال ميديا", "صور مصغّرة", "غلاف سوشيال ميديا", "فلاتر وعدسات",
        "ملصقات تطبيقات التواصل", "تصميم صفحة هبوط", "تصميم موقع", "تصميم تطبيق", "تصميم UI/UX", "تصميم أيقونات",
        "تصميم شعار", "تصميم هوية بصرية", "تصميم بروفايل شركة", "تصميم بطاقة عمل", "تصميم توقيع", "تصميم مخطوطات",
        "تصميم ختم", "تصميم QR Code", "تعديل الصور", "إزالة خلفية الصور", "ترميم الصور القديمة",
        "تعديل صور المنتجات",
        "التحويل إلى Vector", "تصميم بنرات إعلانية", "عبوات وأغلفة منتجات", "تصميم سيرة ذاتية",
        "تصميم عروض تقديمية",
        "تصميم إنفوجرافيك", "شهادات شكر وتقدير", "تنسيق كتب", "تصميم غلاف كتاب", "فلاير وبروشور ورول اب",
        "مطبوعات مكتبية",
        "تصميم منيو", "رسوم كرتونية", "بورتريه وكاريكاتير", "تصميم رموز NFT", "تصميم أزياء", "تصميم تيشرتات",
        "مجوهرات وإكسسوارات", "تصميمات صناعية", "أخرى", "دعوات زواج", "Midjourney", "Stable Diffusion"],

    "صوتيات": ["تعليق صوتي",
        "غناء", "الرد الآلي IVR", "إنتاج وتلحين موسيقي", "الهندسة الصوتية", "إنتاج كتب صوتية", "بودكاست"],

    "هندسة وعمارة": ["تصميم مخططات معمارية", "تصميم داخلي وديكور", "تصميم خارجي وواجهات", "تصميم حدائق ولاند سكيب",
        "تصاميم معمارية تجارية", "إظهار معماري", "تصميم إنشائي", "حساب كميات الإنشاءات",
        "تصميم المخططات الكهربائية",
        "لوحات دوائر PCB", "الأنظمة المدمجة وIOT", "تصميم ميكانيكي", "أنظمة HVAC", "أنظمة المياه والصرف",
        "أنظمة مكافحة الحريق", "أخرى"],

    "تعليم عن بعد": ["تعلم اللغة العربية", "تعلم اللغة الإنجليزية", "تعلم اللغة الفرنسية", "تعلم لغات أخرى",
        "تعلم البرمجة", "تعلم تصميم الجرافيك", "تعلم الفيديو والأنيميشن", "تعلم التسويق الرقمي",
        "شروحات هندسية",
        "تعلم الرياضيات", "شروحات طبية", "تعلم العلوم", "تعلم المحاسبة", "تعلم القرآن الكريم",
        "مساعدة بحل الواجبات",
        "حقائب تدريبية"],

    "كتابة وترجمة": ["الإنجليزية للعربية والعكس", "الفرنسية للعربية والعكس", "التركية للعربية والعكس",
        "الألمانية للعربية والعكس", "الصينية للعربية والعكس", "ترجمة لغات أخرى", "كتابة شعر", "تأليف كتاب",
        "كتابة قصص قصيرة", "كتابة كلمات الأغاني", "سيناريو فيديو", "محتوى بودكاست",
        "سيناريو أفلام ومسلسلات",
        "محتوى تقني", "محتوى علمي", "محتوى رياضي", "محتوى قانوني", "محتوى طبي وصحي", "محتوى ديني وتاريخي",
        "محتوى مالي واقتصادي", "محتوى إخباري وسياسي", "مقالات وتدوينات", "صفحات الموقع الأساسية",
        "محتوى صفحات الهبوط", "كتابة بروفايل الشركات", "محتوى سوشيال ميديا", "رسائل بريد إلكتروني",
        "نصوص إعلانية",
        "وصف منتجات", "خطة محتوى", "خدمات تلخيص", "تدقيق لغوي", "صياغة وفحص اقتباس", "تفريغ نصوص",
        "إعداد وكتابة البحوث",
        "كتابة طلبات المنح", "كتابة السيرة الذاتية", "كتابة الوصف الوظيفي", "أخرى"],

    "تسويق رقمي": ["إدارة حسابات التواصل", "التسويق على فيسبوك",
        "التسويق عبر تويتر", "التسويق عبر اليوتيوب", "التسويق عبر تيك توك", "التسويق عبر الانستقرام",
        "التسويق على سناب شات",
        "التسويق عبر الواتساب", "التسويق عبر التليجرام", "التسويق عبر بنترست", "إعلانات فيس بوك",
        "إعلانات تويتر",
        "إعلانات انستقرام", "إعلانات سناب شات", "إعلانات تيك توك", "إعلانات اليوتيوب", "باك لينك",
        "جيست بوست",
        "تحليل سيو شامل", "بحث كلمات مفتاحية", "تحليل منافسي SEO", "سيو المتاجر الإلكترونية",
        "السيو المحلي Local SEO",
        "سيو اليوتيوب", "خدمات سيو أخرى", "إعلانات المواقع", "الإضافة لأدلة المواقع",
        "التسويق عبر المنتديات",
        "تسويق قواعد البيانات", "تسويق تطبيقات الجوال", "التسويق عبر البريد الإلكتروني",
        "التسويق عبر الشبكات الإعلانية",
        "التسويق عبر محركات البحث", "خطط تسويقية", "استشارات تسويقية", "إضافة أكواد التتبع",
        "تقارير تحليل المواقع"],

    "أعمال": ["أسماء تجارية", "دراسة جدوى", "خطط العمل", "تحليل المنافسين", "استشارات الأعمال",
        "تخطيط موارد المؤسسات ERP",
        "إدارة المشاريع", "إدارة الموارد البشرية", "استشارات إدارية", "بحوث قانونية", "مستندات وعقود قانونية",
        "استشارات قانونية", "التحليل المالي", "محاسبة ومسك الدفاتر", "المحاسبة الضريبية", "برامج محاسبة",
        "استشارات مالية", "القوائم المالية", "البحث عن المنتجات", "إدخال بيانات المنتجات",
        "إدارة المتاجر الإلكترونية",
        "استشارات التجارة الإلكترونية", "خدمة العملاء", "إدارة علاقات العملاء CRM", "تحويل الملفات",
        "البحث على الإنترنت", "أخرى"],

    "برمجة وتطوير": ["إنشاء موقع إلكتروني", "مدونات بلوجر", "إنشاء صفحة هبوط", "تخصيص وتعديل المواقع",
        "إصلاح أخطاء المواقع",
        "نسخ احتياطي ونقل استضافة", "حماية وتأمين المواقع", "اختبارات تجريبية", "إنشاء موقع ووردبريس",
        "تنصيب ووردبريس",
        "تخصيص وتعديل ووردبريس", "تعريب قوالب ووردبريس", "إصلاح مشكلات ووردبريس", "تحسين سرعة ووردبريس",
        "حماية ووردبريس",
        "إضافات ووردبريس", "شوبيفاي", "ووكومرس", "أوبن كارت", "ماجنتو", "سلة", "زد", "فاذرشوبس", "يوكان",
        "إنشاء تطبيق ويب", "واجهات API والتكاملات", "بوابات الدفع الإلكتروني", "تحويل تصميم PSD لموقع",
        "تطبيقات سطح المكتب",
        "بلوك تشين وعملات رقمية", "إضافات المتصفحات", "برمجة CSS و HTML", "برمجة PHP", "برمجة بايثون",
        "برمجة Java و .NET",
        "إنشاء تطبيق", "تعديل التطبيقات", "ريسكين التطبيقات", "إصلاح مشكلات التطبيقات",
        "تحويل الموقع إلى تطبيق",
        "رفع التطبيقات على المتاجر", "إعلانات تطبيقات الجوال", "تطوير ألعاب الجوال", "تطوير ألعاب الفيديو",
        "أنظمة التشغيل والبرمجيات", "أمن وحماية البيانات", "استضافات ونطاقات", "السيرفرات ولينكس", "شبكات",
        "إدارة البريد الإلكتروني", "بوت ديسكورد", "بوت تليجرام", "بوت ماسنجر", "بوت واتساب", "أخرى"],

    "أسلوب حياة": ["سياحة وسفر", "تعليم الطبخ",
        "فنون وحرف", "ألعاب", "توجيه وإرشاد مهني", "استشارات شخصية", "لياقة بدنية", "صحة وتغذية",
        "موضة وجمال"],

    "بيانات": ["استخراج البيانات", "جمع البيانات", "تحليل البيانات", "معالجة البيانات", "علم البيانات وتعلم الآلة",
        "لوحات البيانات",
        "رسوم ومخططات بيانية", "نظم المعلومات الجغرافية GIS", "إدخال بيانات", "قواعد البيانات"]
}
document.addEventListener("DOMContentLoaded", function () {
    const categorySelect = document.getElementById("category_name");
    const serviceSelect = document.getElementById("service_name");

    function updateServiceOptions() {
        const category = categorySelect.value;
        const services = categoryServices[category] || [];

        serviceSelect.innerHTML = "";
        services.forEach(service => {
            const option = document.createElement("option");
            option.value = service;
            option.textContent = service;
            serviceSelect.appendChild(option);
        });

        if (services.length > 0) {
            serviceSelect.value = services[0];
        }
    }

    categorySelect.addEventListener("change", updateServiceOptions);

    updateServiceOptions();
});
document.getElementById("offer-form").addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(event.target);

    const offerData = {
        category_name: formData.get("category_name"),
        service_name: formData.get("service_name"),
        offer_stars: parseFloat(formData.get("offer_stars")),
        offer_raters: parseInt(formData.get("offer_raters")),
        offer_response_time: formData.get("offer_response_time"),
        offer_buyers: parseInt(formData.get("offer_buyers")),
        pending: parseInt(formData.get("pending")),
        duration: formData.get("duration"),
        reviews: parseInt(formData.get("reviews")),
        available_additions: parseInt(formData.get("available_additions")),
        additions_price: parseFloat(formData.get("additions_price")),
        owner_verified: formData.get("owner_verified") === "on",
        owner_level: formData.get("owner_level"),
        owner_stars: parseFloat(formData.get("owner_stars")),
        owner_raters: parseInt(formData.get("owner_raters")),
        owner_completion_rate: parseFloat(formData.get("owner_completion_rate")),
        owner_services: parseInt(formData.get("owner_services")),
        owner_customers: parseInt(formData.get("owner_customers")),
        owner_response_time: formData.get("owner_response_time")
    };

    const resultContainer = document.getElementById("result");

    resultContainer.classList.add("show");

    const baseURL = window.location.origin;

    fetch(`${baseURL}/offer/`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(offerData)
    }).then(response => response.json()).then(data => {
        if (data.status === 201) {
            fetchPrice();
        } else {
            alert("Error: " + data.message);
        }
    });
});

function fetchPrice() {
    const offerId = 0;
    const baseURL = window.location.origin;


    fetch(`${baseURL}/offer/${offerId}`).then(response => response.json()).then(data => {
        document.getElementById("result").textContent = data.message;
    });
}

document.getElementById("owner_verified").addEventListener("change", function () {
    const label = document.getElementById("owner_verified_label");
    if (this.checked) {
        label.textContent = "هوية موثقة";
        label.classList.remove("btn-outline-danger");
        label.classList.add("btn-outline-success");
    } else {
        label.textContent = "هوية غير موثقة";
        label.classList.remove("btn-outline-success");
        label.classList.add("btn-outline-danger");
    }
});

