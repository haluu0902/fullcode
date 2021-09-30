!(function (e) {
  var t = {};
  function n(a) {
    if (t[a]) return t[a].exports;
    var o = (t[a] = { i: a, l: !1, exports: {} });
    return e[a].call(o.exports, o, o.exports, n), (o.l = !0), o.exports;
  }
  (n.m = e),
    (n.c = t),
    (n.d = function (e, t, a) {
      n.o(e, t) || Object.defineProperty(e, t, { enumerable: !0, get: a });
    }),
    (n.r = function (e) {
      "undefined" != typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(e, Symbol.toStringTag, { value: "Module" }),
        Object.defineProperty(e, "__esModule", { value: !0 });
    }),
    (n.t = function (e, t) {
      if ((1 & t && (e = n(e)), 8 & t)) return e;
      if (4 & t && "object" == typeof e && e && e.__esModule) return e;
      var a = Object.create(null);
      if (
        (n.r(a),
        Object.defineProperty(a, "default", { enumerable: !0, value: e }),
        2 & t && "string" != typeof e)
      )
        for (var o in e)
          n.d(
            a,
            o,
            function (t) {
              return e[t];
            }.bind(null, o)
          );
      return a;
    }),
    (n.n = function (e) {
      var t =
        e && e.__esModule
          ? function () {
              return e.default;
            }
          : function () {
              return e;
            };
      return n.d(t, "a", t), t;
    }),
    (n.o = function (e, t) {
      return Object.prototype.hasOwnProperty.call(e, t);
    }),
    (n.p = ""),
    n((n.s = 4));
})([
  function (e, t, n) {
    "use strict";
    n.d(t, "b", function () {
      return c;
    }),
      n.d(t, "c", function () {
        return l;
      }),
      n.d(t, "e", function () {
        return f;
      }),
      n.d(t, "f", function () {
        return p;
      }),
      n.d(t, "g", function () {
        return g;
      }),
      n.d(t, "i", function () {
        return h;
      }),
      n.d(t, "d", function () {
        return E;
      }),
      n.d(t, "h", function () {
        return k;
      }),
      n.d(t, "j", function () {
        return w;
      }),
      n.d(t, "k", function () {
        return I;
      }),
      n.d(t, "l", function () {
        return C;
      }),
      n.d(t, "a", function () {
        return M;
      });
    const a = "undefined" != typeof InstallTrigger,
      o = window.navigator.userAgent.indexOf("Edg") > -1,
      r = a ? "FIREFOX" : o ? "EDGE" : "CHROME";
    let i = !1;
    var s;
    (s = navigator.userAgent || navigator.vendor || window.opera),
      (/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino|android|ipad|playbook|silk/i.test(
        s
      ) ||
        /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw-(n|u)|c55\/|capi|ccwa|cdm-|cell|chtm|cldc|cmd-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc-s|devi|dica|dmob|do(c|p)o|ds(12|-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(-|_)|g1 u|g560|gene|gf-5|g-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd-(m|p|t)|hei-|hi(pt|ta)|hp( i|ip)|hs-c|ht(c(-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i-(20|go|ma)|i230|iac( |-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|-[a-w])|libw|lynx|m1-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|-([1-8]|c))|phil|pire|pl(ay|uc)|pn-2|po(ck|rt|se)|prox|psio|pt-g|qa-a|qc(07|12|21|32|60|-[2-7]|i-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h-|oo|p-)|sdk\/|se(c(-|0|1)|47|mc|nd|ri)|sgh-|shar|sie(-|m)|sk-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h-|v-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl-|tdg-|tel(i|m)|tim-|t-mo|to(pl|sh)|ts(70|m-|m3|m5)|tx-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas-|your|zeto|zte-/i.test(
          s.substr(0, 4)
        )) &&
        (i = !0);
    class c {
      static getInst() {
        return this.inst || (this.inst = new c());
      }
      setItem(e, t) {
        this[e] = t;
      }
      getItem(e) {
        return this[e];
      }
    }
    class l {
      static getDateWithoutTime(e = new Date()) {
        return e.setHours(0, 0, 0, 0), e;
      }
    }
    const u = () => {
      function e() {
        return Math.floor(65536 * (1 + Math.random()))
          .toString(16)
          .substring(1);
      }
      return (
        e() + e() + "-" + e() + "-" + e() + "-" + e() + "-" + e() + e() + e()
      );
    };
    const d =
        /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2}(?:\.\d*))(?:Z|(\+|-)([\d|:]*))?$/,
      m = (e, t) => {
        if ("string" == typeof t) {
          if (d.exec(t)) return new Date(t);
        }
        return t;
      };
    class f {
      static setItem(e, t) {
        "object" == typeof t
          ? t instanceof Date
            ? localStorage.setItem(e, t.toJSON())
            : localStorage.setItem(e, JSON.stringify(t))
          : localStorage.setItem(e, t);
      }
      static getItem(e, t) {
        const n = localStorage.getItem(e);
        if (n && null !== n && "null" !== n && "undefined" !== n) {
          if (d.test(n)) return new Date(n);
          if (!isNaN(Number(n))) return Number(n);
          try {
            return JSON.parse(n, m);
          } catch (e) {
            return n;
          }
        }
        return t || n;
      }
      static removeItem(e) {
        localStorage.removeItem(e);
      }
    }
    class p {
      static log(...e) {
        console.log.apply(null, [
          "%c " + chrome.runtime.getManifest().name,
          "color:cyan",
          ...e,
        ]);
      }
      static warn(...e) {
        console.warn.apply(null, [
          "%c " + chrome.runtime.getManifest().name,
          "color:yellow",
          ...e,
        ]);
      }
      static error(...e) {
        console.error.apply(null, [
          "%c " + chrome.runtime.getManifest().name,
          "color:red",
          ...e,
        ]);
      }
      static info(...e) {
        console.info.apply(null, [
          "%c " + chrome.runtime.getManifest().name,
          "color:blue",
          ...e,
        ]);
      }
      static debug(...e) {
        console.debug.apply(null, [
          "%c " + chrome.runtime.getManifest().name,
          "color:green",
          ...e,
        ]);
      }
    }
    class g {
      static values(e) {
        if (!Array.isArray(e)) throw new TypeError("Param passed is not Array");
        const t = {};
        for (const n of e) t[n] = this._process(n);
        return t;
      }
      static value(e) {
        return this._process(e);
      }
      static _process(e) {
        let t = chrome.runtime.getManifest();
        const n = e.split(".");
        for (const e in n)
          if (n[e]) {
            const a = n[e];
            t && (t = t[a]);
          }
        return t;
      }
    }
    const h = {
      ERROR: "error",
      NOTIFICATIONS: "notifications",
      SOUND: "sound",
      TAB: "tab",
      I18N: "i18n",
      GOOGLE_ANALYTICS: "google-analytics",
      MANIFEST: "manifest",
      EXPORT_DATA: "export-data",
      IMPORT_DATA: "import-data",
      LOCAL_STORAGE: "local-storage",
      BROWSER_ACTION: "browser-action",
      CLOUD_MESSAGING: "cloud-messaging",
      ALARMS: "alarms",
      SCHEDULE: "schedule",
    };
    class w {
      static messageChrome(e) {
        return new Promise((t, n) => {
          if (!window.chrome) return void n("window.chrome not found");
          const a = (e) => {
            window.chrome.runtime.lastError || e.error
              ? n(window.chrome.runtime.lastError || e.error)
              : t(e.result);
          };
          window.react_env
            ? window.chrome.runtime.sendMessage(
                window.react_env[`REACT_APP_${r}_EXTENSION_ID`],
                e,
                a
              )
            : window.chrome.runtime.sendMessage(e, a);
        });
      }
      static async message(e) {
        return await this.messageChrome(e);
      }
    }
    const y = "event",
      v = "error";
    class E extends w {
      static async event(e) {
        return await this.message({
          action: h.GOOGLE_ANALYTICS,
          event: e,
          GAAction: y,
        });
      }
      static async error(e) {
        return await this.message({
          action: h.GOOGLE_ANALYTICS,
          error: e,
          GAAction: v,
        });
      }
    }
    const b = "create",
      T = "update",
      N = "clear";
    class k extends w {
      static async create(e, t = u()) {
        return await this.message({
          action: h.NOTIFICATIONS,
          notificationId: t,
          notificationOptions: e,
          notificationAction: b,
        });
      }
      static async update(e, t = u()) {
        return await this.message({
          action: h.NOTIFICATIONS,
          notificationId: t,
          notificationOptions: e,
          notificationAction: T,
        });
      }
      static async clear(e, t = u()) {
        return await this.message({
          action: h.NOTIFICATIONS,
          notificationId: t,
          notificationOptions: e,
          notificationAction: N,
        });
      }
    }
    class I extends w {
      static async play() {
        return await this.message({ action: h.SOUND });
      }
    }
    const S = "getItem",
      O = "setItem",
      A = "removeItem";
    class C extends w {
      static async getItem(e, t) {
        return await this.message({
          action: h.LOCAL_STORAGE,
          localStorageAction: S,
          key: e,
          fallback: t,
        });
      }
      static async setItem(e, t) {
        return await this.message({
          action: h.LOCAL_STORAGE,
          localStorageAction: O,
          key: e,
          value: t,
        });
      }
      static async removeItem(e) {
        return await this.message({
          action: h.LOCAL_STORAGE,
          localStorageAction: A,
          key: e,
        });
      }
    }
    const x = "setBadgeBackgroundColor",
      L = "setBadgeText",
      R = "setIcon",
      B = "setTitle";
    class M extends w {
      static async setBadgeBackgroundColor(e) {
        return await this.message({
          action: h.BROWSER_ACTION,
          browserAction: x,
          details: e,
        });
      }
      static async setBadgeText(e) {
        return await this.message({
          action: h.BROWSER_ACTION,
          browserAction: L,
          details: e,
        });
      }
      static async setIcon(e) {
        return await this.message({
          action: h.BROWSER_ACTION,
          browserAction: R,
          details: e,
        });
      }
      static async setTitle(e) {
        return await this.message({
          action: h.BROWSER_ACTION,
          browserAction: B,
          details: e,
        });
      }
    }
  },
  function (e, t, n) {
    "use strict";
    n.d(t, "g", function () {
      return c;
    }),
      n.d(t, "a", function () {
        return a;
      }),
      n.d(t, "d", function () {
        return o;
      }),
      n.d(t, "h", function () {
        return r;
      }),
      n.d(t, "i", function () {
        return l;
      }),
      n.d(t, "b", function () {
        return u;
      }),
      n.d(t, "f", function () {
        return d;
      }),
      n.d(t, "j", function () {
        return m;
      }),
      n.d(t, "e", function () {
        return i;
      }),
      n.d(t, "k", function () {
        return s;
      }),
      n.d(t, "c", function () {
        return f;
      });
    const a = {
        "~~ Select Condition ~~": "",
        "= Equals": "Equals",
        "!= Not Equals": "NotEquals",
        "~ Contains": "Contains",
        "!~ Not Contains": "NotContains",
        "> Greater Than": "GreaterThan",
        "< Less Than": "LessThan",
        ">= Greater Than Equals": "GreaterThanEquals",
        "<= Less Than Equals": "LessThanEquals",
      },
      o = { STOP: "stop", SKIP: "skip", RELOAD: "reload" },
      r = {
        elementFinder: "",
        value: "",
        condition: a["~~ Select Condition ~~"],
        valueExtractor: "",
        recheck: 0,
        recheckInterval: 0,
        recheckOption: o.STOP,
      },
      i = { STOP: "stop", SKIP: "skip", RELOAD: "reload" },
      s = {
        retry: 5,
        retryInterval: 1,
        retryOption: i.STOP,
        checkiFrames: !1,
        notifications: {
          onAction: !1,
          onBatch: !1,
          onConfig: !1,
          onError: !1,
          sound: !1,
        },
        pushNotificationKey: "",
      },
      c = {
        name: "",
        initWait: 0,
        elementFinder: "",
        value: "",
        repeat: 0,
        repeatInterval: 0,
        addon: { ...r },
      },
      l = (i.STOP, { refresh: !1, repeat: 0, repeatInterval: 0 }),
      u = { WINDOW: "window", DOCUMENT: "document" },
      d = { AUTO: "auto", MANUAL: "manual" },
      m = {
        name: "",
        url: "",
        initWait: 0,
        startTime: "",
        enable: !0,
        startType: d.AUTO,
        loadType: u.WINDOW,
        hotkey: "Ctrl + Shift + A",
        batch: { ...l },
        actions: [{ ...c }],
      },
      f = {
        SETTINGS: "settings",
        CONFIGS: "configs",
        SHEETS: "sheets",
        INSTALL_DATE: "install_date",
        XPATH: "xpath",
        URL: "url",
      };
  },
  function (e, t, n) {
    "use strict";
    n.d(t, "a", function () {
      return a;
    }),
      n.d(t, "b", function () {
        return o;
      });
    const a = "xpath-selection",
      o = { CONFIG: "config" };
  },
  ,
  function (e, t, n) {
    "use strict";
    n.r(t);
    var a = n(1),
      o = n(0),
      r = n(2);
    const i = async (e, t = "") => {
        if (e) {
          let n = 1e3 * Number(e);
          if (/^\d+(\.\d+)?e\d+(\.\d+)?$/.test(e.toString())) {
            const t = e.toString().split("e");
            n = 1e3 * (Math.floor(Math.random() * Number(t[1])) + Number(t[0]));
          }
          o.f.info(`${t} waiting... ${n / 1e3} sec`),
            await (async (e) => new Promise((t) => setTimeout(t, e)))(n);
        }
      },
      s =
        /^(select|textarea|input|button|label|option|optgroup|fieldset|output)$/gi,
      c = /^(select|textarea|input)$/gi,
      l = /^(select|textarea)$/gi,
      u = /^(radio|checkbox)$/gi;
    class d extends Error {
      constructor(e, t) {
        super(e), (this.name = "CustomError"), (this.title = t);
      }
    }
    class m extends d {
      constructor(e, t) {
        super(e, t), (this.name = "ConfigError");
      }
    }
    var f = (() => {
      const e = async (e, n, a, o, r) => {
          let i = [];
          if (/^(id::|#)/gi.test(n)) {
            const t = e.getElementById(n.replace(/^(id::|#)/gi, ""));
            i = t ? [t] : [];
          } else if (/^ClassName::/gi.test(n))
            i = e.getElementsByClassName(n.replace(/^ClassName::/gi, ""));
          else if (/^Name::/gi.test(n))
            i = e.getElementsByName(n.replace(/^Name::/gi, ""));
          else if (/^TagName::/gi.test(n))
            i = e.getElementsByTagName(n.replace(/^TagName::/gi, ""));
          else if (/^Selector::/gi.test(n)) {
            const t = e.querySelector(n.replace(/^Selector::/gi, ""));
            i = t ? [t] : [];
          } else if (/^SelectorAll::/gi.test(n))
            i = e.querySelectorAll(n.replace(/^SelectorAll::/gi, ""));
          else
            try {
              const t = e.evaluate(
                n,
                e,
                null,
                XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
                null
              );
              if (0 !== t.snapshotLength) {
                let e = 0;
                for (; e < t.snapshotLength; ) i.push(t.snapshotItem(e++));
              }
            } catch (e) {
              throw new m(
                "elementFinder: " + e.message.split(":")[1],
                "Invalid Xpath"
              );
            }
          return i.length ? i : await t(n, a, o, r);
        },
        t = async (t, a, r, s) =>
          a > 0
            ? (a--,
              o.a.setBadgeBackgroundColor({ color: [102, 16, 242, 1] }),
              o.a.setBadgeText({ text: "Retry" }),
              await i(r, "Retry"),
              await e(document, t, a, r))
            : s
            ? n(t)
            : void 0,
        n = (e) => {
          const t = document.getElementsByTagName("iframe"),
            n = [];
          let a;
          for (let o = 0; o < t.length; o++) {
            if (a && 0 !== a.snapshotLength) {
              let e = 0;
              for (; e < a.snapshotLength; ) n.push(a.snapshotItem(e++));
              break;
            }
            if ("about:blank" === t[o].src) {
              const n = t[o].contentDocument;
              n &&
                (a = document.evaluate(
                  e,
                  n,
                  null,
                  XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
                  null
                ));
            }
          }
          return n.length ? n : void 0;
        },
        r = (e, t) => {
          if (e === a.e.RELOAD)
            "complete" === document.readyState
              ? location.reload()
              : window.addEventListener("load", function () {
                  location.reload();
                });
          else {
            if (e === a.e.STOP) throw new m("elementFinder: " + t, "Not Found");
            o.f.log(`elementFinder: ${t} not found and action is SKIP`);
          }
        };
      return {
        start: async (t, n = {}) => {
          if (!t)
            throw new m("elementFinder can not be empty!", "Element Finder");
          const {
              retryOption: i,
              retryInterval: s,
              retry: c,
              checkiFrames: l,
            } = { ...o.b.getInst().getItem(a.c.SETTINGS), ...n },
            u = await e(document, t, c, s, l);
          return (u && 0 !== u.snapshotLength) || r(i, t), u;
        },
      };
    })();
    class p extends d {
      constructor(e, t) {
        super(e, t), (this.name = "SystemError");
      }
    }
    var g = ((e) => {
      const t = async (
          { elementFinder: t, value: a, condition: o, valueExtractor: i, ...c },
          l
        ) => {
          const u = await e.start(t, l),
            d = r(u, i);
          return (
            s(d, o, a) ||
            (await n({
              elementFinder: t,
              value: a,
              condition: o,
              valueExtractor: i,
              ...c,
            }))
          );
        },
        n = async ({
          elementFinder: e,
          value: n,
          condition: r,
          recheck: s,
          recheckInterval: c,
          recheckOption: l,
          valueExtractor: u,
        }) => {
          if (s > 0)
            return (
              s--,
              o.a.setBadgeBackgroundColor({ color: [13, 202, 240, 1] }),
              o.a.setBadgeText({ text: "Recheck" }),
              await i(c, "Addon Recheck"),
              await t({
                elementFinder: e,
                value: n,
                condition: r,
                recheck: s,
                recheckInterval: c,
                recheckOption: l,
                valueExtractor: u,
              })
            );
          if (l !== a.d.RELOAD) {
            if (l === a.d.STOP)
              throw new m(
                `elementFinder: ${e}\nvalue: ${n}\ncondition: ${r}`,
                "Not Matched"
              );
            return o.f.info("Value not matched and action is SKIP"), !1;
          }
          "complete" === document.readyState
            ? location.reload()
            : window.addEventListener("load", function () {
                location.reload();
              });
        },
        r = (e, t) => {
          const n = e[0];
          let a;
          if (
            ((a = l.test(n.nodeName)
              ? n.value
              : "INPUT" === n.nodeName
              ? u.test(n.type)
                ? n.checked
                : n.value
              : "DIV" === n.nodeName && n.isContentEditable
              ? n.textContent
              : n.innerText),
            t)
          ) {
            const e = RegExp(t).exec(a);
            return (e && e[0]) || a;
          }
          return a;
        },
        s = (e, t, n) => {
          if (/than/gi.test(t) && (isNaN(Number(e)) || isNaN(Number(n))))
            throw new m(
              "Greater || Less can only compare number",
              "Wrong Comparison"
            );
          switch (t) {
            case a.a["= Equals"]:
              return new RegExp(`^${n}$`, "gi").test(e);
            case a.a["!= Not Equals"]:
              return !new RegExp(`^${n}$`, "gi").test(e);
            case a.a["~ Contains"]:
              return new RegExp("" + n, "gi").test(e);
            case a.a["!~ Not Contains"]:
              return !new RegExp("" + n, "gi").test(e);
            case a.a["> Greater Than"]:
              return Number(e) > Number(n);
            case a.a[">= Greater Than Equals"]:
              return Number(e) >= Number(n);
            case a.a["< Less Than"]:
              return Number(e) < Number(n);
            case a.a["<= Less Than Equals"]:
              return Number(e) <= Number(n);
            default:
              throw new p(
                "Addon Condition not found",
                t + " condition not found"
              );
          }
        };
      return {
        check: async ({
          elementFinder: e,
          value: n,
          condition: a,
          ...o
        } = {}) =>
          !(e && n && a) ||
          (await t({ elementFinder: e, value: n, condition: a, ...o })),
      };
    })(f);
    var h = (() => {
      const e = () => ({
        screenX: 10,
        screenY: 10,
        clientX: 10,
        clientY: 10,
        bubbles: !0,
        cancelable: !0,
        view: window,
      });
      return {
        getFillEvent: () => {
          const e = document.createEvent("HTMLEvents");
          return e.initEvent("change", !1, !0), e;
        },
        getMouseEvent: () => new MouseEvent("click", e()),
        getMouseEventProperties: e,
        getKeyboardEventProperties: ({
          key: e = "",
          code: t = "",
          location: n = 0,
          ctrlKey: a = !1,
          shiftKey: o = !1,
          altKey: r = !1,
          metaKey: i = !1,
          repeat: s = !1,
          isComposing: c = !1,
          charCode: l = 0,
          keyCode: u = 0,
          which: d = 0,
        }) => ({
          key: e,
          code: t,
          location: n,
          ctrlKey: a,
          shiftKey: o,
          altKey: r,
          metaKey: i,
          repeat: s,
          isComposing: c,
          charCode: l,
          keyCode: u,
          which: d,
        }),
        loopElements: (e, t, n) => {
          for (const a of e) n(a, t);
        },
        getVerifiedEvents: (e, t) => {
          if (!t)
            throw new p(
              "Event is blank!",
              "Event cant be blank | null | undefined"
            );
          let n;
          t = t.split("::")[1];
          try {
            const a = JSON.parse(t);
            Array.isArray(a)
              ? (n = a.filter(
                  (t) => -1 !== e.indexOf("string" == typeof t ? t : t.type)
                ))
              : -1 !== e.indexOf(a.type) && (n = [a]);
          } catch (a) {
            const o = t.replace(/\W/g, "");
            -1 !== e.indexOf(o) && (n = [o]);
          }
          if (n) return n;
          throw new m("value: " + t, "Invalid Events");
        },
      };
    })();
    const w = ["blur", "click", "focus", "select", "submit", "remove", "clear"],
      y = ((e) => {
        const t = (e, t) => {
          if (!(e instanceof HTMLElement))
            throw new m("elementFinder: " + e, "Not HTMLElement");
          t.forEach((t) => {
            switch ("string" == typeof t ? t : t.type) {
              case "blur":
                e.blur();
                break;
              case "click":
                e.click();
                break;
              case "focus":
                e.focus();
                break;
              case "submit":
                if (e instanceof HTMLFormElement) e.submit();
                else {
                  if (!s.test(e.nodeName))
                    throw new m(
                      "elementFinder: " + e,
                      "Invalid Element for submit"
                    );
                  e.form.submit();
                }
                break;
              case "select":
                e.select();
                break;
              case "remove":
                e.remove();
                break;
              case "clear":
                if (!c.test(e.nodeName))
                  throw new m(
                    "elementFinder: " + e,
                    "Invalid Element for clear"
                  );
                e.value = "";
                break;
              default:
                throw new p("Unhandled Event", t);
            }
          });
        };
        return {
          start: (n, a) => {
            const o = (void 0)._getVerifiedEvents(w, a);
            e.loopElements(n, o, t);
          },
        };
      })(h),
      v = ["reload", "href", "replace"],
      E = ((e) => {
        const t = (e, t) => {
          e.forEach((e) => {
            switch (e) {
              case "reload":
                location.reload();
                break;
              case "href":
                window.location.href = t.split("::")[2];
                break;
              case "replace":
                window.location.replace(t.split("::")[2]);
                break;
              default:
                throw new p("Unhandled Event", event);
            }
          });
        };
        return {
          start: (n) => {
            const a = e.getVerifiedEvents(v, n);
            t(a, n);
          },
        };
      })(h),
      b = [
        "contextmenu",
        "mousedown",
        "mouseup",
        "pointerdown",
        "pointerup",
        "dblclick",
        "click",
        "mouseover",
        "mouseout",
        "mouseenter",
        "mouseleave",
        "mousemove",
      ],
      T = ((e) => {
        const t = (t, n) => {
          n.forEach((n) => {
            "string" == typeof n
              ? t.dispatchEvent(new MouseEvent(n, e.getMouseEventProperties()))
              : t.dispatchEvent(
                  new MouseEvent(n.type, {
                    ...e.getMouseEventProperties(),
                    ...n,
                  })
                );
          });
        };
        return {
          start: (n, a) => {
            const o = e.getVerifiedEvents(b, a);
            e.loopElements(n, o, t);
          },
        };
      })(h),
      N = ((e) => {
        const t = (e) => {
            if (!e)
              throw new p(
                "Event is blank!",
                "Event cant be blank | null | undefined"
              );
            let t;
            e = e.split("::")[1];
            try {
              const {
                value: n,
                delay: a = 0,
                shiftKey: o,
                ctrlKey: r,
                metaKey: i,
                altKey: s,
              } = JSON.parse(e);
              if (!n) throw new m(e, "Invalid Events");
              t = n
                .split("")
                .map((e) => ({
                  key: e,
                  delay: a,
                  shiftKey: o,
                  ctrlKey: r,
                  metaKey: i,
                  altKey: s,
                }));
            } catch (n) {
              o.f.error(n), (t = e.split("").map((e) => ({ key: e })));
            }
            if (t) return t;
            throw new m(e, "Invalid Events");
          },
          n = async (t, n) => {
            for (const a of n)
              t.dispatchEvent(
                new KeyboardEvent("keydown", {
                  ...e.getKeyboardEventProperties(a),
                })
              ),
                (t.value += a.key),
                t.dispatchEvent(
                  new KeyboardEvent("keyup", {
                    ...e.getKeyboardEventProperties(a),
                  })
                ),
                a.delay && (await i(a.delay, "Key Event"));
          };
        return {
          start: (a, o) => {
            const r = t(o);
            e.loopElements(a, r, n);
          },
        };
      })(h),
      k = ((e) => {
        const t = (e) => ("::empty" === e ? "" : e),
          n = (t, n) => {
            "SELECT" === t.nodeName ||
            "TEXTAREA" === t.nodeName ||
            ("INPUT" === t.nodeName && !u.test(t.type))
              ? ((t.value = n), t.dispatchEvent(e.getFillEvent()))
              : "DIV" === t.nodeName && t.isContentEditable
              ? (t.textContent = n)
              : "OPTION" === t.nodeName
              ? (t.selected = !0)
              : ["mouseover", "mousedown", "mouseup", "click"].forEach((n) => {
                  t.dispatchEvent(
                    new MouseEvent(n, e.getMouseEventProperties())
                  );
                }),
              t.focus();
          };
        return {
          start: (a, o) => {
            (o = t(o)), e.loopElements(a, o, n);
          },
        };
      })(h),
      I = [
        "Top",
        "Bottom",
        "Left",
        "Right",
        "TopLeft",
        "BottomLeft",
        "BottomRight",
        "TopRight",
        "XPath",
      ],
      S = ((e) => {
        const t = (e) => {
            let t = 0,
              n = 0;
            -1 !== e.indexOf("Right") && (t = document.body.scrollWidth),
              -1 !== e.indexOf("Bottom") && (n = document.body.scrollHeight),
              window.scrollTo(t, n);
          },
          n = (e) => {
            e[0].scrollIntoView();
          };
        return {
          start: (a, o) => {
            if (/xpath/gi.test(o)) n(a);
            else {
              const n = e.getVerifiedEvents(I, o)[0];
              t(n);
            }
          },
        };
      })(h),
      O = /^Sheet::[\w|-]+::\w[$|\d]$/i,
      A = /^Query::/i;
    var C = ((e) => {
      let t, n, a;
      const r = (e, t, n) => {
          if (e.match(O))
            try {
              const [, a, o] = e.split("::"),
                r = "$" === o[1] ? t : parseInt(o[1]),
                i = o[0].charCodeAt(0) - 65;
              if (!n[a])
                throw new m(`Sheet: "${a}" not found!`, "Sheet not found");
              if (!n[a][r])
                throw new m(
                  `Sheet "${a}" do not have Row ${r}`,
                  "Sheet row not found"
                );
              if (i < 0 || i > 25)
                throw new m(
                  `Invalid column letter "${o[0]}" in value:${e}`,
                  "Sheet column invalid"
                );
              e = n[a][r][i];
            } catch (e) {
              o.f.error(e), o.d.error({ name: e.name, stack: e.stack });
            }
          else if (e.match(A)) {
            const [, t] = e.split("::"),
              n = new URLSearchParams(window.location.search);
            n.has(t) && (e = n.get(t));
          } else e = e.replaceAll("<batchRepeat>", t);
          return e;
        },
        s = async (e) => {
          if (e)
            /^scrollto::/gi.test(e)
              ? S.start(t, e)
              : /^clickevents::/gi.test(e) || /^mouseevents::/gi.test(e)
              ? T.start(t, e)
              : /^formevents::/gi.test(e)
              ? y.start(t, e)
              : /^locationcommand::/gi.test(e)
              ? E.start(e)
              : /^keyevents::/gi.test(e)
              ? N.start(t, e)
              : k.start(t, e);
          else
            for (const e of t)
              ["mouseover", "mousedown", "mouseup", "click"].forEach((t) => {
                e.dispatchEvent(new MouseEvent(t, h.getMouseEventProperties()));
              });
          await c(e);
        },
        c = async (e) => {
          (n > 0 || n < -1) && (n--, await i(a, "Action Repeat"), s(e));
        };
      return {
        start: async (o, c, l) => {
          if (
            (await i(o.initWait, "Action Wait"),
            await g.check(o.addon, o.settings))
          ) {
            const i = o.elementFinder.replaceAll("<batchRepeat>", c);
            if (((t = await e.start(i, o.settings)), t)) {
              (n = o.repeat - 1), (a = o.repeatInterval);
              const e = r(o.value, c, l);
              await s(e);
            }
          }
        },
      };
    })(f);
    var x = {
      start: async (e, t, n) => {
        const r = o.b.getInst().getItem(a.c.SETTINGS);
        for (let a = 0; a < e.length; a++)
          o.a.setBadgeBackgroundColor({ color: [25, 135, 84, 1] }),
            o.a.setBadgeText({ text: `${t}-${a}` }),
            o.a.setTitle({ title: `Batch:${t} Action:${a}` }),
            await C.start(e[a], t, n),
            r.notifications.onAction &&
              (o.h.create({
                title: "Action Completed",
                message: e[a].elementFinder,
              }),
              r.notifications.sound && o.k.play());
      },
    };
    var L = (() => {
      let e, t, n;
      const r = () => {
          "complete" === document.readyState
            ? location.reload()
            : window.addEventListener("load", function () {
                location.reload();
              });
        },
        s = async () => {
          const r = o.b.getInst().getItem(a.c.SETTINGS);
          if (e.repeat > 0)
            for (let a = 0; a < e.repeat; a++)
              e.repeatInterval && (await i(e.repeatInterval, "Batch Repeat")),
                await x.start(t, a + 1, n),
                r.notifications.onBatch &&
                  (o.h.create({
                    title: "Batch Completed",
                    message: `#${a + 1} Batch`,
                  }),
                  r.notifications.sound && o.k.play());
          else if (e.repeat < -1) {
            let a = 1;
            for (;;)
              e.repeatInterval && (await i(e.repeatInterval, "Batch Repeat")),
                await x.start(t, a, n),
                a++;
          }
        };
      return {
        start: async (a, o, i) => {
          (e = a),
            (t = o),
            (n = i),
            await x.start(o, 0, n),
            e.refresh ? r() : await s();
        },
      };
    })();
    const R = {
      setup: (e, t) => {
        document.addEventListener(
          "keydown",
          ({ ctrlKey: n, shiftKey: a, altKey: o, code: r }) => {
            const i = e.split("+").pop().trim();
            r.replace(/key/gi, "") === i &&
              /ctrl/gi.test(e) === n &&
              /alt/gi.test(e) === o &&
              /shift/gi.test(e) === a &&
              t();
          }
        );
      },
    };
    var B = (() => {
      let e;
      const t = async (t, r, i) => {
          try {
            const r = await o.l.getItem(a.c.SHEETS, []);
            await L.start(e.batch, e.actions, n(r)),
              o.a.setBadgeBackgroundColor({ color: [25, 135, 84, 1] }),
              o.a.setBadgeText({ text: "Done" }),
              t &&
                (o.h.create({
                  title: "Config Completed",
                  message: e.name || e.url,
                }),
                i && o.k.play());
          } catch (t) {
            if (!(t instanceof m)) throw t;
            {
              const n = {
                title: t.title,
                message: `url : ${e.url}\n${t.message}`,
              };
              o.a.setBadgeBackgroundColor({ color: [220, 53, 69, 1] }),
                o.a.setBadgeText({ text: "Error" }),
                r ? (o.h.create(n), i && o.k.play()) : o.f.error(n);
            }
          }
        },
        n = (e) => {
          const t = {};
          if (Array.isArray(e)) for (const n of e) t[n.name] = n.rows;
          return t;
        },
        r = async () => {
          e.startTime && e.startTime.match(/^\d{2}:\d{2}:\d{2}:\d{3}$/)
            ? await s()
            : await i(e.initWait, "Configuration");
        },
        s = async () => {
          var t = new Date();
          t.setHours(Number(e.startTime.split(":")[0])),
            t.setMinutes(Number(e.startTime.split(":")[1])),
            t.setSeconds(Number(e.startTime.split(":")[2])),
            t.setMilliseconds(Number(e.startTime.split(":")[3])),
            await new Promise((e) =>
              setTimeout(e, t.getTime() - new Date().getTime())
            );
        };
      return {
        getConfig: async (
          { notifications: { onConfig: n, onError: i, sound: s } },
          c
        ) => {
          c &&
            ((e = c),
            o.a.setBadgeBackgroundColor({ color: [13, 110, 253, 1] }),
            e.startType === a.f.MANUAL || e.startManually
              ? (o.a.setBadgeText({ text: "Manual" }),
                o.a.setTitle({ title: "Start Manually" }),
                R.setup(e.hotkey || a.j.hotkey, t.bind(void 0, n, i, s)))
              : (o.a.setBadgeText({ text: "Auto" }),
                o.a.setTitle({ title: "Start Automatically" }),
                await r(),
                t(n, i, s)));
        },
      };
    })();
    const M = (() => {
      const e = (e) => {
          2 === e.button && t(n(e.target), e);
        },
        t = (e, t) => {
          o.l.setItem(a.c.URL, t.view.document.URL), o.l.setItem(a.c.XPATH, e);
        },
        n = (e) => {
          if (e) {
            if ("" !== e.id) return `//*[@id="${e.id}"]`;
            if (e === document.body) return "/html/" + e.tagName.toLowerCase();
            var t = 1,
              a = e.parentNode.childNodes;
            if (a)
              for (var o = 0; o < a.length; o++) {
                var r = a[o];
                if (r === e)
                  return n(e.parentNode) + `/${e.tagName.toLowerCase()}[${t}]`;
                1 === r.nodeType && r.tagName === e.tagName && t++;
              }
          }
          return "";
        };
      return {
        setup: () => {
          document.addEventListener("mousedown", e, !0);
        },
      };
    })();
    async function P(e) {
      try {
        const t = await o.j.message({
          action: r.b.CONFIG,
          href: document.location.href,
          frameElement: window.top !== window.self,
        });
        if (t) {
          const n = await o.l.getItem(a.c.SETTINGS, a.k);
          o.b.getInst().setItem(a.c.SETTINGS, n),
            (t.loadType || n.loadType || a.b.WINDOW) === e &&
              (await B.getConfig(n, t));
        }
      } catch (e) {
        o.f.error(e), o.d.error({ name: e.name, stack: e.stack });
      }
    }
    document.addEventListener("DOMContentLoaded", function () {
      P(a.b.DOCUMENT);
    }),
      window.addEventListener("load", function () {
        P(a.b.WINDOW);
      }),
      M.setup();
  },
]);
