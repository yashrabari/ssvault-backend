"use strict";(self.webpackChunkweb=self.webpackChunkweb||[]).push([[109],{8586:function(n,A,e){e.d(A,{ZB:function(){return x},iA:function(){return b},sh:function(){return w},U8:function(){return C}});var t=e(885),o=e(168),i=e(2791),r=e(7691),d=(e(6159),e(4687)),a=e.n(d);e(6622);var s=e(1068),u=e(5861);var c,l,g=e(8529),f=(e(2482),e(184)),h=r.ZP.div(c||(c=(0,o.Z)(["\n  width: 621px;\n  background: #f5f5f5;\n  border-radius: 20px;\n  display: flex;\n  flex-direction: column;\n  align-items: center;\n  margin: 16px 0;\n  padding: 20px;\n"])));function x(n){n.navigate,n.subscription,n.setbuddies;var A=n.addBuddies,e=(n.token,n.store),o=(0,s.d)(),r=o.unSetModal,d=(o.setModal,(0,i.useState)("")),c=(0,t.Z)(d,2),l=c[0],x=c[1],p=(0,i.useState)(""),B=(0,t.Z)(p,2),b=B[0],w=B[1],C=(0,i.useState)(""),v=(0,t.Z)(C,2),U=v[0],k=v[1],m=(0,i.useState)(""),Q=(0,t.Z)(m,2),R=Q[0],E=Q[1],I=(0,i.useState)(!1),j=(0,t.Z)(I,2),P=j[0],S=j[1];(0,i.useEffect)((function(){return e.subscribe((function(){var n,A,t,o,i=null===(n=e.getState())||void 0===n||null===(A=n.buddies)||void 0===A?void 0:A.error,r=null===(t=e.getState())||void 0===t||null===(o=t.buddies)||void 0===o?void 0:o.success;E(i),S(r)}))}),[e]);var y=function(){A(l,U).unwrap().then((function(n){e.dispatch(function(){var n=(0,u.Z)(a().mark((function n(A){return a().wrap((function(n){for(;;)switch(n.prev=n.next){case 0:A({type:"ADD_BUDDY_REQUEST"});try{A({type:"ADD_BUDDY_SUCCESS"})}catch(R){A({type:"ADD_BUDDY_ERROR",payload:R})}case 2:case"end":return n.stop()}}),n)})));return function(A){return n.apply(this,arguments)}}()),r()})).catch((function(n){console.error(n),w(n.response.data.email[0])}))};return(0,f.jsxs)(g.sg,{width:"100%",justifyContent:"space-between",alignItems:"center",height:"",children:[(0,f.jsx)(g.Dx,{fontWeight:"700",margin:"16px 0",children:"Add New Buddy"}),(0,f.jsxs)(h,{children:[(0,f.jsx)(g.BZ,{label:"Email of the buddy",placeholder:"Enter your buddies Email",value:l,onChange:function(n){return x(n.target.value)}}),(0,f.jsx)(g.Ph,{label:"Select relationship",placeholder:"Select the relationship",options:["Marriage partner","Power of attorney","other"],value:U,onChange:function(n){return k(n.target.value)}})]}),R&&(0,f.jsx)(g.nv,{width:"",color:"#FF5F5F",children:"Unable to add buddy"}),P&&(0,f.jsx)(g.nv,{width:"",color:"#00A652",children:"Buddy added successfully"}),"Enter a valid email address."===b&&(0,f.jsx)(g.nv,{width:"",color:"#FF5F5F",children:b}),"This field may not be blank."===b&&(0,f.jsx)(g.nv,{width:"",color:"#FF5F5F",children:"Email cannot be blank"}),(0,f.jsxs)(g.X2,{justifyContent:"flex-end",children:[(0,f.jsx)(g.zx,{width:"151px",height:"50px",color:"#FBBC05",onClick:y,children:"Send Invite Link"}),(0,f.jsx)(g.zx,{width:"151px",height:"50px",color:"#00A652",onClick:function(){return y()},children:"Add Buddy"})]})]})}var p,B,b=r.ZP.table(l||(l=(0,o.Z)(["\n  background: #fff;\n  border-radius: ",";\n  border-collapse: collapse;\n  overflow: visible;\n"])),(function(n){return n.borderRadius?n.borderRadius:"10px"})),w=r.ZP.tr(p||(p=(0,o.Z)(['\n  text-align: left;\n  font-size: 16px;\n  font-weight: 400;\n  font-family: "TT Commons";\n  color: #000000;\n  border-bottom: 1px solid rgba(0, 0, 0, 0.05);\n  td {\n    padding: 18px ;\n  }\n']))),C=r.ZP.tr(B||(B=(0,o.Z)(['\n  text-align: left;\n  font-size: 16px;\n  font-weight: 400;\n  font-family: "TT Commons";\n  color: #00000080;\n  border-bottom: 1px solid rgba(0, 0, 0, 0.05);\n  th {\n    padding: 18px;\n  }\n'])))},2482:function(n,A,e){e.d(A,{Z:function(){return u}});var t,o=e(168),i=(e(2791),e(7691)),r=e(1068),d=e(8529),a=e(184),s=i.ZP.div(t||(t=(0,o.Z)(["\n  width: 621px;\n  background: #f5f5f5;\n  border-radius: 20px;\n  display: flex;\n  flex-direction: column;\n  align-items: center;\n  margin: 16px 0;\n  padding: 20px;\n"])));function u(n){var A=n.message,e=void 0===A?"":A,t=n.buttonText,o=void 0===t?"OK":t,i=n.onSubmit,u=(0,r.d)().unSetModal;return(0,a.jsx)(d.sg,{width:"100%",justifyContent:"space-between",alignItems:"center",height:"",children:(0,a.jsxs)(s,{children:[(0,a.jsx)(d.Dx,{fontWeight:"700",margin:"16px 0",children:e}),(0,a.jsx)(d.X2,{justifyContent:"center",children:(0,a.jsx)(d.zx,{width:"151px",height:"50px",color:"#00A652",onClick:function(){return u(),void(i&&i())},children:o})})]})})}},7820:function(n,A,e){e.d(A,{Z:function(){return B}});var t,o,i,r,d=e(885),a=e(168),s=e(2791),u=e(71),c=e(1033),l=(e(815),e(7691)),g=l.ZP.button(t||(t=(0,a.Z)(["\n  outline: none;\n  background: transparent;\n  border: none;\n  position: relative;\n  cursor: pointer;\n"]))),f=l.ZP.div(o||(o=(0,a.Z)(["\n  box-sizing: border-box;\n  position: absolute;\n  top: 70px;\n  right: -30px;\n\n  z-index: 50;\n\n  background: #ffffff;\n  box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.08);\n  border-radius: 10px;\n\n  overflow: hidden;\n"]))),h=l.ZP.div(i||(i=(0,a.Z)(["\n  width: ",';\n  height: 100%;\n\n  padding: 10px;\n\n  font-family: "TT Commons";\n  font-size: 18px;\n  text-align: left;\n  color: #000;\n\n  :hover {\n    background: #ebebeb6b;\n  }\n'])),(function(n){return n.width})),x=e(184),p=l.ZP.div(r||(r=(0,a.Z)(['\n  align-self: start;\n  width: 100%;\n  height: 40px;\n  margin: 0;  \n  font-family: "TT Commons";\n  font-style: normal;\n  font-weight: 400;\n  font-size: 18px;\n  line-height: 28px;\n\n  display: flex;\n  justify-content: flex-start;\n  align-items: center;\n'])));function B(n){var A=n.options,e=(0,s.useState)(!1),t=(0,d.Z)(e,2),o=t[0],i=t[1],r=(0,s.useRef)(null);return(0,x.jsxs)(g,{ref:r,onBlur:function(){return i(!1)},children:[(0,x.jsx)(c.Z,{backgroundColor:o?"#00A652":"",onClick:function(){i((function(n){return!n}))},children:(0,x.jsx)(u.Fuo,{color:o?"white":"",size:20})}),o&&(0,x.jsx)(f,{children:A.map((function(n,A){return(0,x.jsx)(h,{width:"152px",onClick:function(){n.onClick(),r.current.blur()},children:(0,x.jsxs)(p,{children:[(0,x.jsx)("img",{src:n.Icon,width:"20px",height:"20px",style:{marginRight:"5px"}}),n.text]})},A)}))})]})}},144:function(n){n.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAACxLAAAsSwGlPZapAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAU8SURBVHgB7Z2Ndds2EIC/9nUAbdDboN6g6AbeINwgzgRiJ0g6gbVBsgGdCexMQHUCpROkREi9KDIBAgTAP+F7756eZAqA7oDD8QDCkMlkMplMJpPJZDKZTCaTuRV+YfncNaIakUZ+797Tvb/k2MjXTr50718aeSLjxa6Rh0aqRk6NfAuUU1dWwWujZToulf4tsZyNkaFV/J44Pd1X6q5u4QaZU/EmQ9wMivZHz634PkMoJmbKKOjc6x/8vvY9qtHRzJfu9aX77Hh1nXSi69GR0p/d6w4/PjTyd1fHolC0jdMi+CH49fpTV48iHNXIwbP+moXNDQWvG6kcv6uvc/X1FWndwD3ukdapu34R9PWeyuF7b1mG4q8R3A3h6zKjs8M8TG3sWejEd0GBm2vaMyOCvwFclK99vO8EmQKhnSMWOxIEPwO4KH/2Yd2DbtNQuxUzILgbYEj5emK7Iw7n9MUD8SIW3Tb9u2ztFyZGcDPAkPJr4irqMrKKaVjBbgT9t0ldpzBsgCmVr3mmP5KKhWAPnd8zIYLdAFMrH0tdMbljIfOBYFbsHMqHaQygsU3Mk7kiwa7k1MpXjTzinkrQ132kjfFjKOiDpa6SCRDmUb4iPGuqvx8a8u4s7TgxwSgQplf+HoIUfy0VYYpSzDgKhHUr/yw6cgoxQkWCUeCyHiAM533OfB649j9an3o0/L2g9fep0HW/YxwKc6j7ris7CUL83qgM9dQJ6nKp25UKs4tLhhBfCX0NLrC7Nj2Zugx1Rf+NWgxlKUu5ySbjHfENUPfU82y5VvDnQBplme6QkyYYbT0qxgiwGVkxDl2mSVkhK12m+4KKhAxlCX17v1yVryzXhnAgfm9VhjJPjOA3x+teGvmLcbsMrvmE+46DI2EcDZ+H/IYn2vbvesrU+nlhhZgSX6EjQBHfBWkq4o+sWUkxB5w5XJV3IBzTPJDsXmAKTL2qb87wRff4kngp5IL+tn5ixZTYJ+6CZSzia1K5zFmxhY2+osvRobN2CbGWKi8RNmgAjcvOhDGi1weEuJjqWj0laYygR8Ub4rFZA2hK0hhBSywjbNoAmoI02dFYe3s2b4AzOoQ8EDcfVRGGGMqtyXxHaN2YLapSjEcZynxmxaTaamgyQshd6z1pRtZspNxqWBK/t5bEN+qspNxqKJgn47FUhjJXm4xLHVHELt/k1hQrxfSDhHCEuCNAxSzvV5bB0fB5QThv8KtziMLw+SoXYs6Y8uuhk3GKKKg2lFewYhRY71z3+LkjYfgohDGGvbeUJ6ycCgbvYGPJR8ZhamOsiG1WhGkO7xibCxJLmQUboSC9AQrGURnKq9kYBWlGwonxyi8s5ZZsEKFd4I6l/Irxk6RgjnxqNn7gk45UdLioUxU+o+JyTVgRxoEb6/0umBQSm7eWumpumCkMsJjHVEPQ2cFHxh3yZKPitUJiLoYI9uXQVaSd35NuwrqpowrGoDA3PqaizitosRRiyx2dDS2sgAK7/1ziwoXL6V6hu6onw+WxpkeW0Zt0W6/d5Vo6jRWXbYY18+ZRFG57j0pWiutez4ppR4NiRYf2haL9ps+xlSn9rMLv2ErFRhD8D059JN7BrTpu90ll1Ew0Il2OKoiFnuxK2mjDh6+0662f+fnY4uPVdcKPB+W0/MG4hwr/6drp+iDh6lDkw7sXQckyDHHq2rL4u9sUCPMZ4qYV30fBdP/CJGb6YnMIP4wR85/4LFLpU0ZBY1G00YzQRja7TuTqumP3qiOlf7v3T6x8x1omk8lkMplMJpPJZDKZTGY7/A82OM6oc8J/6AAAAABJRU5ErkJggg=="},9478:function(n){n.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAACxLAAAsSwGlPZapAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAKLSURBVHgB7Z3dkdpAEAbbLgdwIRDaZXJkgB2BNpOzI7AzIARCOIMPuc4YIa20uzMjfV01j+yquiWqQPyAEEIIIYQQQgjhhJfznK5zQDSlO8/bzXSIJtyT7zLCE++X6SvDB9x6lj5ddBP2cBFhd54jfsTfzp58uoz1zSMc8Su/vxJy6GbsYRbhGd/ycwN0C/YxifAT/wG+Mo1uZJ10HVcRvEgeOvP3TKNjXH5PwlGEoYOIRI78noSTCNEDzJHfk3AQIXKAJfJ7EsYRogYYk58jLxVaZxYRA0yRXzrCnkpEC5Ajv2SE3BeDk4kUYI78nAiP1t98gDH5iWXP5WPrT30xmE2EAFPk9yTyI+SsXxzvAebISUyPYCoffAdYIicxHsFcPvgNUEJOGlnDXD74DFDyzEw4lg/+ApSU35NwKh98BaghvyfhUD74CVBTfov1Z+MhwGblg32ATcsH2wCbl3/BKoDkX7EIIPkfaB1A8m9oGUDy79AqgOQP0CJAFPkvGHyJo3aAKPIPdx67pwE1A0SRf+F05/HV7gN/pFaASPKh7onYfOMDseTDygKciCUfVhYgmnzYSIAl1JQPCvCQ2vJBAQZpIR8U4C6t5IMC/EdL+aAA/9BaPijAXyzkgwL8wUo+bCTAkknURQGwk//omENuHE3+o2MOufGjN+M8yoeVBdgTSz6sLMCFy5fa5lwJOT/QUZIiHj6Rz1vBtSJTxMNnhCkKYIwCGKMAxiiAMQpgjAIYowDGKIAxCmCMAhijAMYogDEKYMwXytHkZsTamHMFfEcM8YtM5gT4gRjiGw24/HnPkTI30dc0RxqyQxFu5e8w4JkYf2lSa155/0DAE0IIIYQQQgghhBBCjPAbPQ3CoXpQcsQAAAAASUVORK5CYII="},1484:function(n){n.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAACxLAAAsSwGlPZapAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAIXSURBVHgB7d3rTRtREIbhL1EKIB24hJTkTtgOSCrwSQXQgUugBEqADsyOLBAXG2TLe+Zy3keanyB5XpuVdlmvBAAAAAAAAHzvap7rebbz7Baax3luhE9W8zxoucV/nEl4p+fyXz4JJf3U6dbafwLg5F593/02f4VXvf/0TCrsly7nh3Cyc44BuCACOCOAMwI4I4AzAjgjgDMCOCOAMwI4Gz3An3k22l9UWiuJYyfOsllpf7Lv7WvYKIEqAZoOv47wEaoEuNPx1xI6QpUAk76+FhE2QpUApilhhEoBTFOyCNUCmKZEESoGME1JIlQNYJoSRKgcwDQFj1A9gGkKHGGEAKYpaIRRApimgBFGCmCagkUYLYBpChShR4BrfT5VHH026mTpADfKtfi3M+lE5/xD7e6Cv+sQe+dfKaeneX6f8gNcE3YWMcA/5fVfHSx9DDB2R0y2g3BTJz0CRLNRkOVL4wUItXxprADhli+NEyDk8qUxAoRdvlQ/QOjlS7UDhF++qRogxfJNxQBplm+qBUi1fFMpQLrlmyoB1kq4fFMlwFYJl2+qBGhKuHxTJYDdH/bxlHdTApUOwivtl34rpy+GinhNeChcE3ZGAGcEcEYAZwRwRgBnBHBGAGcEcEYAZ5cMsFtgeILGAVsts+yvZhJeTeofoOwTNM5hd688iACuVuobgSdoHLHWso80Kf8EDQAAAAAAAIzjGUidc0QUiQCuAAAAAElFTkSuQmCC"},629:function(n){n.exports="data:image/png;base64,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"}}]);
//# sourceMappingURL=109.51277d1a.chunk.js.map