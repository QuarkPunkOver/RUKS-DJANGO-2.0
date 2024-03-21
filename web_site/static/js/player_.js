function kinobd_key(e) {
  if (e && (e.key || e.keyCode)) {
    var t = "";
    if (
      ("Enter" === e.key ||
        (13 === e.keyCode ? (t = "fullscreen") : "Left" === e.key) ||
        "ArrowLeft" === e.key ||
        (37 === e.keyCode ? (t = "prev") : "Right" === e.key) ||
        "ArrowRight" === e.key ||
        (39 === e.keyCode ? (t = "next") : "Up" === e.key) ||
        "ArrowUp" === e.key ||
        (38 === e.keyCode ? (t = "up") : "Down" === e.key) ||
        "ArrowDown" === e.key ||
        (40 === e.keyCode ? (t = "down") : "0" === e.key) ||
        (48 === e.keyCode ? (t = "0") : "1" === e.key) ||
        (49 === e.keyCode ? (t = "1") : "2" === e.key) ||
        (50 === e.keyCode ? (t = "2") : "3" === e.key) ||
        (51 === e.keyCode ? (t = "3") : "4" === e.key) ||
        (52 === e.keyCode ? (t = "4") : "5" === e.key) ||
        (53 === e.keyCode ? (t = "5") : "6" === e.key) ||
        (54 === e.keyCode ? (t = "6") : "7" === e.key) ||
        (55 === e.keyCode ? (t = "7") : "8" === e.key) ||
        ((56 === e.keyCode ? (t = "8") : "9" !== e.key) && 57 !== e.keyCode) ||
        (t = "9"),
      !t || ("up" !== t && "down" !== t))
    )
      if (t && "fullscreen" === t) kb_fullscreen();
      else {
        var n = document.querySelectorAll(
          '[data-event]:not([style*="display:none"]):not([style*="display: none"]'
        );
        if (n && n.length)
          for (var o = 0; o < n.length; o++)
            if (
              t &&
              n[o].dataset.event === t &&
              "function" == typeof n[o].onclick
            )
              return void n[o].onclick.apply(n[o]);
      }
    else {
      var a = document.querySelector(".kinobd-active");
      if (a && a.dataset && a.dataset.event && parseInt(a.dataset.event)) {
        var i =
          "up" === t
            ? document.querySelector(
                '[data-event="' +
                  (parseInt(a.dataset.event) - 1) +
                  '"]:not([style*="display:none"]):not([style*="display: none"]'
              )
            : document.querySelector(
                '[data-event="' +
                  (parseInt(a.dataset.event) + 1) +
                  '"]:not([style*="display:none"]):not([style*="display: none"]'
              );
        if (i || "up" !== t)
          if (i || "down" !== t)
            i && "function" == typeof i.onclick && i.onclick.apply(i);
          else {
            var r = document.querySelector(
              '[data-event="next"]:not([style*="display:none"]):not([style*="display: none"]'
            );
            r && "function" == typeof r.onclick && r.onclick.apply(r);
          }
        else {
          var l = document.querySelector(
            '[data-event="prev"]:not([style*="display:none"]):not([style*="display: none"]'
          );
          l && "function" == typeof l.onclick && l.onclick.apply(l);
        }
      }
    }
  }
}
function kbp(e) {
  var t,
    n,
    o,
    a,
    i,
    r,
    l,
    s = !1,
    d = "",
    u = e && e.getAttribute("data-kbd") ? e.getAttribute("data-kbd") : "kinobd";
  if (
    !(r = document.querySelector("#" + u)) &&
    !(r = document.querySelector("#kinobd-online"))
  ) {
    if (!(r = document.querySelector("#kinobd-torrent"))) return !1;
    s = !0;
  }
  for (
    var c = document.createElement("div"),
      p = Array.prototype.slice.call(r.attributes);
    (n = p.pop());

  )
    c.setAttribute(n.nodeName, n.nodeValue);
  (c.innerHTML = r.innerHTML), r.parentNode.replaceChild(c, r);
  var y = [].slice.call(c.attributes).reduce(function (e, t) {
    return (
      /^data-/.test(t.name) &&
        (e[t.name.substr(5)] = decodeURIComponent(t.value)),
      e
    );
  }, {});
  e &&
    e.attributes &&
    [].slice.call(e.attributes).reduce(function (e, t) {
      /^data-/.test(t.name) &&
        (y[t.name.substr(5)] = decodeURIComponent(t.value));
    }, {}),
    ((y.title && /Ñ‚Ñ€ÐµÐ¹Ð»ÐµÑ€|trailer|teaser/i.test(y.title)) || s) &&
      (y.player = "trailer"),
    (y.player =
      (y.title && /Ñ‚Ñ€ÐµÐ¹Ð»ÐµÑ€|trailer|teaser/i.test(y.title)) || s
        ? "trailer"
        : y.player
        ? y.player
        : "collaps,voidboost,cdnmovies,alloha,ashdi,videocdn,original,ia,youtube,hdvb,iframe,pleer,ustore,kodik,kholobok,kinotochka,ext,trailer,vk,nf");
  var m =
      y.bg && y.bg.replace(/[^0-9a-z]/gi, "")
        ? y.bg.replace(/[^0-9a-z]/gi, "")
        : "2A3440",
    b = y.url
      ? decodeURIComponent(y.url).trim() +
        (decodeURIComponent(y.url).indexOf("?") + 1 ? "&" : "?") +
        "cache" +
        Math.random().toString().substr(2, 3)
      : "//kinobd.net/playerdata?c" + Math.random().toString().substr(2, 3);
  y.url = null;
  var g = y.loading
    ? decodeURIComponent(y.loading).trim()
    : "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+PHN2ZyB4bWxuczpzdmc9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjAiIHdpZHRoPSIxMDBweCIgaGVpZ2h0PSIxMDBweCIgdmlld0JveD0iMCAwIDEyOCAxMjgiIHhtbDpzcGFjZT0icHJlc2VydmUiPjxnPjxwYXRoIGQ9Ik0uNiA1Ny41NGM1LjczLTYuMjMgMTcuMzMtMTUuNSAzMy42Ni0xMi4zNUM1NS40IDQ4LjUgNjQgNjMuOTUgNjQgNjMuOTVTNDIuNDIgNjUgMzAuMjggODMuNjNhMzguNjMgMzguNjMgMCAwIDAtMy40IDMyLjE1IDY0LjQ3IDY0LjQ3IDAgMCAxLTUuNTItNC40NEE2My42NCA2My42NCAwIDAgMSAuNiA1Ny41NHoiIGZpbGw9IiNmZmNiMDIiLz48cGF0aCBkPSJNNjUuMzIgMjkuMDVjNy42NSAxOS45OC0xLjQ0IDM1LjE4LTEuNDQgMzUuMThTNTIuMiA0Ni4wNSAzMC4wMyA0NC44NUEzOC42IDM4LjYgMCAwIDAgLjU2IDU3LjkzIDYzLjggNjMuOCAwIDAgMSAzNy41NiA2YzguMiAxLjggMjIuMjYgNy4xNiAyNy43NiAyMy4wNXoiIGZpbGw9IiNmZjllMDIiLz48cGF0aCBkPSJNOTQuOTIgNDcuN2MtMTMuNDggMTYuNjMtMzEuMiAxNi4zNi0zMS4yIDE2LjM2czkuOTItMTkuMi0uMTMtMzlhMzguNiAzOC42IDAgMCAwLTI2LjE4LTE5IDYzLjc4IDYzLjc4IDAgMCAxIDYzLjUyIDYuMDNjMi41NiA4IDQuOTggMjIuODUtNi4wNSAzNS42eiIgZmlsbD0iI2ZmNGI0MiIvPjxwYXRoIGQ9Ik05My41MiA4Mi41M0M3Mi4zOCA3OS4xNyA2My43NSA2My43IDYzLjc1IDYzLjdzMjEuNi0xLjAyIDMzLjctMTkuNjNhMzguNiAzOC42IDAgMCAwIDMuNDMtMzIuMDQgNjQuMzMgNjQuMzMgMCAwIDEgNS43NCA0LjYgNjMuNjMgNjMuNjMgMCAwIDEgMjAuODIgNTMuMjZjLTUuNjIgNi4yLTE3LjM0IDE1LjgtMzMuOTQgMTIuNnoiIGZpbGw9IiNjMDYzZDYiLz48cGF0aCBkPSJNNjIuNSA5OWMtNy42NS0xOS45OCAxLjQ0LTM1LjE3IDEuNDQtMzUuMTdTNzUuNTYgODEuNiA5Ny43NCA4Mi44YTM5LjEgMzkuMSAwIDAgMCAyOS43My0xMy4wMyA2My44IDYzLjggMCAwIDEtMzcuMTYgNTIuM2MtOC4yLTEuOC0yMi4yNS03LjE1LTI3LjgtMjMuMDZ6IiBmaWxsPSIjMTdhNGY2Ii8+PHBhdGggZD0iTTI2LjY0IDExNS42M0MyNCAxMDcuNiAyMS42IDkzLjA2IDMyLjUgODAuNWMxMy40OC0xNi42MiAzMS41OC0xNi41NSAzMS41OC0xNi41NXMtOS42IDE5LjA2LjQ0IDM4Ljg2YTM4LjgyIDM4LjgyIDAgMCAwIDI2LjA1IDE5LjE3IDYzLjc4IDYzLjc4IDAgMCAxLTYzLjkzLTYuM3oiIGZpbGw9IiM0ZmNhMjQiLz48YW5pbWF0ZVRyYW5zZm9ybSBhdHRyaWJ1dGVOYW1lPSJ0cmFuc2Zvcm0iIHR5cGU9InJvdGF0ZSIgZnJvbT0iMCA2NCA2NCIgdG89IjM2MCA2NCA2NCIgZHVyPSIxNTAwbXMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIj48L2FuaW1hdGVUcmFuc2Zvcm0+PC9nPjwvc3ZnPg==";
  y.loading = null;
  var M =
      y.language && !/ru/i.test(y.language)
        ? {
            trailer: "TRAILER",
            torrent: "DOWNLOAD",
            lookbase: "Ukrainian translation",
            nf: "NOT FOUND",
            next: "NEXT",
            prev: "PREV",
          }
        : {
            trailer: "Ð¢Ð Ð•Ð™Ð›Ð•Ð ",
            torrent: "Ð¡ÐšÐÐ§ÐÐ¢Ð¬",
            lookbase: "Ð£ÐºÑ€Ð°Ð¸Ð½ÑÐºÐ¸Ð¹ Ð¿ÐµÑ€ÐµÐ²Ð¾Ð´",
            nf: "ÐÐ• ÐÐÐ™Ð”Ð•ÐÐž",
            next: "Ð’ÐŸÐ•Ð Ð•Ð”",
            prev: "ÐÐÐ—ÐÐ”",
          },
    f = {};
  for (var k in ((y.button = y.button
    ? y.button
    : "videocdn: {Q} {T}, voidboost: {Q} {T}, hdvb: {Q} {T}, ashdi: {Q} {T}, bazon: {Q} {T}, original: {Q} {T}, ia: {Q} {T}, youtube: {Q} {T}, ustore: {Q} {T}, alloha: {Q} {T}, kodik: {Q} {T}, iframe: {Q} {T}, collaps: {Q} {T}, kinotochka: {Q} {T}, cdnmovies: {Q} {T}"),
  y.button &&
    y.button.split(",").forEach(function (e) {
      var t = e.split(":");
      2 === t.length &&
        t[0] &&
        t[1] &&
        (f[t[0].trim().toLowerCase()] = t[1].trim());
    }),
  (y.button_limit =
    y.button_limit && parseInt(y.button_limit) < 5
      ? parseInt(y.button_limit)
      : 5),
  (y.button_size =
    y.button_size && parseFloat(y.button_size) ? parseFloat(y.button_size) : 1),
  (y.separator = y.separator ? y.separator : ","),
  y))
    y.hasOwnProperty(k) && y[k]
      ? (d += d
          ? "&" + k + "=" + encodeURIComponent(y[k])
          : k + "=" + encodeURIComponent(y[k]))
      : (y[k] = "");
  if (!(y.kinopoisk || y.title || y.imdb || y.tmdb || y.inid)) return !1;
  y.tv && document.addEventListener("keydown", kinobd_key),
    y.resize &&
      (window.addEventListener("orientationchange", kb_resize, !1),
      window.addEventListener("resize", kb_resize, !1));
  var I = document.querySelector("#kinobd-loading");
  I && I.parentNode.removeChild(I);
  var N = document.querySelector("#kinobd-buttons");
  N && N.parentNode.removeChild(N);
  var v = document.querySelector("#kinobd-iframe");
  v && v.parentNode.removeChild(v);
  var h = document.querySelectorAll("[data-kbd]");
  for (var C in h)
    if (h.hasOwnProperty(C) && h[C]) {
      var A = document.querySelector("#" + h[C].getAttribute("data-kbd"));
      A && A.removeAttribute("style");
    }
  var j = document.head || document.getElementsByTagName("head")[0],
    w =
      "#kinobd-loading{z-index:9999;position:absolute;left:0;top:0;width:100%;height:100%;background:#" +
      m +
      " url(" +
      g +
      ") 50% 50% no-repeat}#kinobd-buttons{position:absolute;z-index:9999;right:0;top:30px;text-align:left}#kinobd-buttons:hover{right:0!important}#kinobd-buttons div{font-family:Verdana,sans-serif;font-weight:normal;text-shadow:none;line-height:normal;font-size:" +
      12 * y.button_size +
      "px;color:#fff;background:#" +
      m +
      ";border-radius:5px 0 0 5px;padding:10px;margin:5px 0 5px 5px;opacity:.7;}#kinobd-buttons div:hover,#kinobd-buttons div.kinobd-active{color:#fff;background:#" +
      m +
      ";cursor:pointer;opacity:1}";
  ((l = document.createElement("style")).type = "text/css"),
    l.styleSheet
      ? (l.styleSheet.cssText = w)
      : l.appendChild(document.createTextNode(w)),
    j.appendChild(l),
    (i = document.createElement("div")).setAttribute("id", "kinobd-loading"),
    (c.innerHTML = ""),
    c.appendChild(i),
    (a = document.createElement("iframe")).setAttribute("id", "kinobd-iframe"),
    a.setAttribute("frameborder", "0"),
    a.setAttribute("allowfullscreen", "allowfullscreen"),
    c.appendChild(a),
    (o = parseInt(c.offsetWidth)
      ? parseInt(c.offsetWidth)
      : c.parentNode && parseInt(c.parentNode.offsetWidth)
      ? parseInt(c.parentNode.offsetWidth)
      : 610);
  var z =
    "width:100%;height:" +
    (t =
      c.parentNode &&
      c.parentNode.tagName &&
      "body" === c.parentNode.tagName.toLowerCase()
        ? Math.max(
            document.body.scrollHeight,
            document.body.offsetHeight,
            document.documentElement.clientHeight,
            document.documentElement.scrollHeight,
            document.documentElement.offsetHeight
          )
        : parseInt(c.offsetHeight) && parseInt(c.offsetHeight) < 370
        ? c.parentNode &&
          parseInt(c.parentNode.offsetHeight) &&
          parseInt(c.parentNode.offsetHeight) >= 370
          ? parseInt(c.parentNode.offsetHeight)
          : 370
        : parseInt(c.offsetHeight) && o / 3 < parseInt(c.offsetHeight)
        ? parseInt(c.offsetHeight)
        : c.parentNode &&
          parseInt(c.parentNode.offsetHeight) &&
          o / 3 < parseInt(c.parentNode.offsetHeight)
        ? parseInt(c.parentNode.offsetHeight)
        : o / 2) +
    "px;border:0;margin:0;padding:0;overflow:hidden;position:relative;";
  a.setAttribute("style", z),
    a.setAttribute("width", o),
    a.setAttribute("height", t),
    c.setAttribute("style", z),
    kb_get(b, d, function (e) {
      var t = !0,
        n = document.createElement("div");
      n.setAttribute("id", "kinobd-buttons");
      var o = y.player.split(y.separator);
      if (/\/\/|%2F%2F/i.test(y.player)) {
        for (var a = [], i = 0; i < o.length; i++) {
          var r = o[i].match(/^(.*?)(http.*|\/\/.*)$/i);
          r && r[1] && r[1].trim() && a.push(r[1].trim());
        }
        if (a.length) o = a;
        else {
          for (var l = Object.keys(e), s = [], d = 0; d < o.length; d++)
            for (var u = 0; u < l.length; u++)
              o[d].toLowerCase().indexOf(l[u].toLowerCase()) + 1 &&
                s.push(l[u]);
          o = s;
        }
      }
      for (var p = 0, m = 0, b = o.length; m < b; m++) {
        var g = o[m].toLowerCase().trim();
        if (e.hasOwnProperty(g) && e[g] && e[g].iframe) {
          (e[g].quality = e[g].quality ? e[g].quality.replace(/"/g, "'") : ""),
            (e[g].translate = e[g].translate
              ? e[g].translate.replace(/"/g, "'")
              : "");
          var k = document.createElement("div");
          if (
            (k.setAttribute(
              "onclick",
              'kb_player("' +
                encodeURIComponent(e[g].iframe) +
                '", "' +
                e[g].quality +
                '", "' +
                e[g].translate +
                '", this, "' +
                y.button_size +
                '", null, "' +
                g +
                '")'
            ),
            (k.dataset.event = "" + (p + 1)),
            (k.dataset.page = Math.ceil((p + 1) / y.button_limit) + ""),
            (k.dataset.iframe = e[g].iframe),
            (k.dataset.quality = e[g].quality),
            (k.dataset.translate = e[g].translate),
            f.hasOwnProperty(g) && f[g])
          ) {
            var I = e[g].quality
                ? e[g].quality.toUpperCase().search(/TS|TC|SCR|CAM/gi) + 1
                  ? "Ð­ÐšÐ ÐÐ"
                  : e[g].quality.toUpperCase().search(/720P/gi) + 1
                  ? "720P"
                  : e[g].quality.toUpperCase().search(/1080P/gi) + 1
                  ? "1080P"
                  : e[g].quality
                      .toUpperCase()
                      .replace(
                        /\s?Ð¥ÐžÐ ÐžÐ¨Ð•Ð•\s?|\s?Ð¡Ð Ð•Ð”ÐÐ•Ð•\s?|\s?ÐŸÐ›ÐžÐ¥ÐžÐ•\s?/gi,
                        ""
                      )
                : "",
              N = e[g].translate
                ? /Ð”Ð£Ð‘Ð›/i.test(e[g].translate)
                  ? "Ð”Ð£Ð‘Ð›Ð¯Ð–"
                  : /ÐŸÐ ÐžÐ¤/i.test(e[g].translate)
                  ? "ÐŸÐ ÐžÐ¤."
                  : /Ð›Ð®Ð‘Ð˜Ð¢/i.test(e[g].translate)
                  ? "Ð›Ð®Ð‘Ð˜Ð¢."
                  : /ÐÐ’Ð¢ÐžÐ /i.test(e[g].translate)
                  ? "ÐÐ’Ð¢ÐžÐ ."
                  : /ÐœÐÐžÐ“ÐžÐ“ÐžÐ›/i.test(e[g].translate)
                  ? "ÐœÐÐžÐ“ÐžÐ“ÐžÐ›."
                  : /ÐžÐ”ÐÐžÐ“ÐžÐ›/i.test(e[g].translate)
                  ? "ÐžÐ”ÐÐžÐ“ÐžÐ›."
                  : /Ð”Ð’Ð£Ð¥Ð“ÐžÐ›/i.test(e[g].translate)
                  ? "Ð”Ð’Ð£Ð¥Ð“ÐžÐ›."
                  : /ÐžÐ Ð˜Ð“Ð˜ÐÐÐ›/i.test(e[g].translate)
                  ? "ÐžÐ Ð˜Ð“Ð˜ÐÐÐ›"
                  : /(ENG|ORIG|Ð¡Ð£Ð‘Ð¢)/i.test(e[g].translate)
                  ? y.language && /en/i.test(y.language)
                    ? "ENGLISH"
                    : "Ð¡Ð£Ð‘Ð¢Ð˜Ð¢Ð˜Ð Ð«"
                  : e[g].translate.toUpperCase()
                : "";
            p++,
              (f[g] = f[g]
                .replace("{N}", p)
                .replace("{Q}", I)
                .replace("{T}", N)
                .replace(/\s+/g, " ")
                .replace(/(^\s*)|(\s*)$/g, "")),
              (f[g] = f[g] ? f[g] : g.toUpperCase()),
              (k.innerText = p + " â¤ï¸ " + f[g]);
          } else
            "trailer" === g
              ? (p++, (k.innerText = p + " â¤ï¸ " + M.trailer.toUpperCase()))
              : "torrent" === g
              ? (p++, (k.innerText = p + " â¤ï¸ " + M.torrent.toUpperCase()))
              : "vk" === g
              ? (p++, (k.innerText = p + " â¤ï¸ " + M.vk.toUpperCase()))
              : "nf" === g
              ? (p++, (k.innerText = p + " â¤ï¸ " + M.nf.toUpperCase()))
              : "lookbase" === g
              ? (p++, (k.innerText = p + " â¤ï¸ " + M.lookbase.toUpperCase()))
              : (p++, (k.innerText = p + " â¤ï¸ " + g.toUpperCase()));
          if (
            (t &&
              (kb_player(
                e[g].iframe,
                e[g].quality,
                e[g].translate,
                k,
                n,
                y.button_size,
                g
              ),
              (t = !1)),
            n.appendChild(k),
            p &&
              !(p % y.button_limit) &&
              e[o[m + 1].toLowerCase().trim()] &&
              e[o[m - 1].toLowerCase().trim()])
          ) {
            var v = document.createElement("div");
            v.setAttribute(
              "onclick",
              "kb_page(" +
                Math.ceil((p + 1) / y.button_limit) +
                ', "' +
                y.button_size +
                '");kb_player("' +
                encodeURIComponent(e[o[m + 1].toLowerCase().trim()].iframe) +
                '", "' +
                e[o[m + 1].toLowerCase().trim()].quality +
                '", "' +
                e[o[m + 1].toLowerCase().trim()].translate +
                '", document.querySelector(\'[data-event="' +
                (p + 1) +
                '"]\'), "' +
                y.button_size +
                '", "' +
                o[m + 1] +
                '")'
            ),
              (v.dataset.event = "next"),
              (v.dataset.page = Math.ceil(p / y.button_limit) + ""),
              (v.innerText = "-â¤ï¸ " + M.next),
              n.appendChild(v);
            var h = document.createElement("div");
            h.setAttribute(
              "onclick",
              "kb_page(" +
                Math.ceil(p / y.button_limit) +
                ', "' +
                y.button_size +
                '");kb_player("' +
                encodeURIComponent(e[o[m - 1].toLowerCase().trim()].iframe) +
                '", "' +
                e[o[m - 1].toLowerCase().trim()].quality +
                '", "' +
                e[o[m - 1].toLowerCase().trim()].translate +
                '", document.querySelector(\'[data-event="' +
                p +
                '"]\'), "' +
                y.button_size +
                '", "' +
                o[m + 1] +
                '")'
            ),
              (h.dataset.event = "prev"),
              (h.dataset.page = Math.ceil((p + 1) / y.button_limit) + ""),
              (h.innerText = "â—„- " + M.prev),
              n.appendChild(h);
          }
        }
      }
      p < 1
        ? (document.querySelector("#kinobd-loading").style.display = "none")
        : p > 1 &&
          (c.appendChild(n),
          o.length > y.button_limit && kb_page(1, y.button_size));
    });
}
function kb_player(e, t, n, o, a, i, r) {
  window.parent.postMessage({ quality: t, translate: n }, "*");
  var l = document.querySelector("#kinobd-loading");
  (l.style.display = "block"),
    setTimeout(function () {
      l.style.display = "none";
    }, 1e3);
  var s = document.querySelector("#kinobd-iframe"),
    d = Date.now();
  if (
    ((s.onload = function () {
      var e = Date.now();
      kb_ping(r, e - d);
    }),
    (s.style.display = "block"),
    s.setAttribute("src", decodeURIComponent(e)),
    s.setAttribute("class", ""),
    "function" == typeof o.setAttribute)
  ) {
    var u = document.querySelectorAll(".kinobd-active");
    if (u) for (var c = 0; c < u.length; c++) u[c].setAttribute("class", "");
    o.setAttribute("class", "kinobd-active");
  }
  var p = a || document.querySelector("#kinobd-buttons");
  (i = i ? parseFloat(i) : 1),
    p &&
      ((p.style = p.style ? p.style : {}),
      p.style && "object" == typeof p.style
        ? (p.style.right = "0")
        : (p.style = { right: "0" }),
      setTimeout(function () {
        var e = setInterval(function () {
          parseInt((p.style && p.style.right) || "0") >
          -parseInt(p.offsetWidth) + 30 * i
            ? (p.style.right = parseInt(p.style.right) - 1 + "px")
            : clearInterval(e);
        }, 5);
      }, 5e3));
}
function kb_page(e, t) {
  var n = document.querySelectorAll("div[data-page]");
  if (n) for (var o = 0; o < n.length; o++) n[o].style.display = "none";
  var a = document.querySelectorAll('div[data-page="' + e + '"]');
  if (a) for (var i = 0; i < a.length; i++) a[i].style.display = "block";
  var r = document.querySelector("#kinobd-buttons");
  (t = t ? parseFloat(t) : 1),
    r &&
      ((r.style.right = "0"),
      setTimeout(function () {
        var e = setInterval(function () {
          parseInt((r.style && r.style.right) || "0") >
          -parseInt(r.offsetWidth) + 30 * t
            ? (r.style.right = parseInt(r.style.right) - 1 + "px")
            : clearInterval(e);
        }, 5);
      }, 5e3));
}
function kb_get(e, t, n) {
  var o = new XMLHttpRequest();
  (o.onreadystatechange = function () {
    4 === o.readyState &&
      (200 === o.status
        ? n(kb_json(o.responseText), o.responseText)
        : n({}, ""));
  }),
    o.open("POST", e, !0),
    o.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"),
    o.setRequestHeader("X-Re", window.location.href),
    o.send(t);
}
function kb_ping(e, t = null) {
  var n = document.getElementById("kinobd"),
    o = [
      "inid=",
      n.dataset.inid ? encodeURIComponent(n.dataset.inid) : "",
      "&kinopoisk=",
      n.dataset.kinopoisk ? encodeURIComponent(n.dataset.kinopoisk) : "",
      "&imdb=",
      n.dataset.imdb ? encodeURIComponent(n.dataset.imdb) : "",
      "&provider=",
      e,
      "&loadtime=",
      t,
    ].join(""),
    a = new XMLHttpRequest();
  (a.onreadystatechange = function () {
    4 === a.readyState && a.status;
  }),
    a.open("POST", "//kinobd.net/ping", !0),
    a.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"),
    a.setRequestHeader("X-Re", window.location.href),
    a.send(o);
}
function kb_json(e) {
  try {
    var t = JSON.parse(e);
    if (t && "object" == typeof t) return t;
  } catch (e) {}
  return {};
}
function kb_fullscreen() {
  var e =
      document.fullscreenElement ||
      document.webkitFullscreenElement ||
      document.mozFullScreenElement ||
      document.msFullscreenElement,
    t = document.querySelector("#kinobd-iframe");
  e
    ? document.exitFullscreen
      ? document.exitFullscreen()
      : document.webkitExitFullscreen
      ? document.webkitExitFullscreen()
      : document.mozCancelFullScreen
      ? document.mozCancelFullScreen()
      : document.msExitFullscreen && document.msExitFullscreen()
    : t.requestFullscreen
    ? t.requestFullscreen()
    : t.mozRequestFullScreen
    ? t.mozRequestFullScreen()
    : t.webkitRequestFullScreen
    ? t.webkitRequestFullScreen()
    : t.msRequestFullscreen && t.msRequestFullscreen();
}
function kb_resize() {
  var e = document.querySelector("#kinobd-iframe");
  if (
    e &&
    e.parentNode &&
    e.parentNode.parentNode &&
    e.parentNode.parentNode.offsetWidth
  ) {
    var t = parseInt(e.parentNode.parentNode.offsetWidth);
    (e.style.width = t + "px"),
      e.setAttribute("width", t.toString()),
      (e.parentNode.style.width = t + "px");
  }
}
(window.onresize = function (e) {
  kb_resize();
}),
  (function () {
    var e = document.querySelectorAll("[data-kbd]");
    if (e && e.length)
      for (var t in e)
        e.hasOwnProperty(t) &&
          e[t] &&
          e[t].addEventListener("click", function () {
            kbp(this);
          });
    else kbp();
  })();
