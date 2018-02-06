
(function() {

    // DATA
    let data = [
        {-% for e in data.data %-}
        [ '__$e[0]$__', `__$e[1]$__` ],
        {-% endfor %-}
    ];
    console.log(data);

    let uuid = "__$data.uuid$__";
    let sel = __$data.selection$__;

    let width = __$data.width$__;
    let height = __$data.height$__;
    let borderPx = __$data.borderPx$__;
    let borderColor = "__$data.borderColor$__";
    let tabBackgroundColor = "__$data.tabBackgroundColor$__";
    let buttonMargin = __$data.buttonMargin$__;
    let buttonPaddingVert = __$data.buttonPaddingVert$__;
    let buttonPaddingHori = __$data.buttonPaddingHori$__;
    let buttonBorderColor = "__$data.buttonBorderColor$__";
    let imageWidthPerCent = __$data.imageWidthPerCent$__;

    let buttonColorBase = "__$data.buttonColorBase$__";
    let buttonColorHover = "__$data.buttonColorHover$__";
    let buttonColorActive = "__$data.buttonColorActive$__";

    // BUILD CSS
    var style = document.createElement("style");
    document.head.appendChild(style);
    let sheet = style.sheet;

    // let uuid = Math.round(Math.random() * 1e9);
    // console.log(uuid);

    sheet.insertRule(
    `.tab-${uuid} { 
            display: flex;
            flex-direction: row;
            justify-content: center;

            width: ${width}px;
            overflow: hidden;
            border: ${borderPx}px solid ${borderColor};
            background-color: ${tabBackgroundColor};
        }`,
    0
    );

    sheet.insertRule(
    `.tab-${uuid} button { 
            background-color: __$data.buttonColorBase$__;
            border: 1px solid ${buttonBorderColor};
            font-size: 13px;
            white-space: nowrap;
            text-align: center;
            cursor: pointer;
            padding: ${buttonPaddingHori}px ${buttonPaddingVert}px;
            margin: ${buttonMargin}px;
        }`,
    0
    );

    sheet.insertRule(
    `.tab-${uuid} button:hover { 
            background-color: __$data.buttonColorHover$__;
        }`,
    0
    );

    sheet.insertRule(
    `.tab-${uuid} button.active { 
            background-color: __$data.buttonColorActive$__;
        }`,
    0
    );

    sheet.insertRule(
    `.image-container-${uuid} { 
            display: flex;
            flex-direction: row;
            justify-content: center;
            width: ${width}px;
            height: ${height}px;
            padding: 5px 0px;
            border: ${borderPx}px solid ${borderColor};
            border-top: none;
        }`,
    0
    );

    sheet.insertRule(
    `.image-${uuid} { 
            margin: auto;
            width: __$data.imageWidthPerCent$__%;
        }`,
    0
    );

    let container = document.getElementById(`container-${uuid}`);

    let tabs = document.createElement("div");
    tabs.className = `tab-${uuid}`;
    container.appendChild(tabs);

    let images = document.createElement("div");
    images.className = `image-container-${uuid}`;
    container.appendChild(images);

    let arr_button = [];
    let arr_image = [];

    for (let datum of data) {
    let img = document.createElement("img");
    img.src = datum[1];
    img.src = `data:image/png;base64,${datum[1]}`;

    img.className = `image-${uuid}`;
    img.style.display = "none";

    let button = document.createElement("button");
    button.innerHTML = datum[0];

    tabs.appendChild(button);
    images.appendChild(img);

    arr_button.push(button);
    arr_image.push(img);
    }

    for (let [k, datum] of data.entries()) {
    let button = arr_button[k];

    let button_clicked = function() {
        console.log(datum[0] + " clicked");

        for (let [i, img] of arr_image.entries()) {
        if (i != k) {
            img.style.display = "none";
            arr_button[i].classList.remove("active");
        } else {
            img.style.display = "block";
            arr_button[i].classList.add("active");
        }
        }
    };
    button.addEventListener("click", button_clicked);
    }

    for (let [k, img] of arr_image.entries()) {
    if (k == sel) {
        img.style.display = "block";
        arr_button[k].classList.add("active");
    }
    }
})()
