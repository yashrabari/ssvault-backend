"use strict";(self.webpackChunkweb=self.webpackChunkweb||[]).push([[625],{8625:function(e,n,i){i.r(n),i.d(n,{default:function(){return w}});var t=i(4942),s=i(1413),o=i(885),c=i(2791),d=i(71),r=i(2978),u=i(8529),l=i(8586),a=i(1068),h=i(6871),x=i(9970),f=i(629),j=i(1484),b=i(144),p=i(9478),g=i(7820),m=i(2482),v=i(9696),k=i(3953),C=i(184);function w(){var e=(0,h.s0)(),n=(0,r.I0)(),i=(0,r.v9)((function(e){return e.reducer.auth.token})),w=(0,c.useState)([]),S=(0,o.Z)(w,2),Z=S[0],y=S[1],I=(0,r.oR)(),A=(0,a.d)().setModal,B=(0,c.useState)({}),M=(0,o.Z)(B,2),N=M[0],P=M[1],E=(0,v.UV)(),X=E.data,F=E.isLoading,J=(E.isSuccess,(0,v.X)()),L=J.data,R=J.isLoading,U=(J.isSuccess,(0,v.dt)()),z=(0,o.Z)(U,1)[0],D=(0,v.Mg)(),O=(0,o.Z)(D,1)[0],T=(0,c.useMemo)((function(){return null!==X&&void 0!==X&&X.results?X.results[0]:null}),[X]);(0,c.useEffect)((function(){y(L)}),[L]),(0,c.useEffect)((function(){var e={};Z.forEach((function(n){var i=n.id;e[i]=!1})),P(e)}),[P]);var K=function(){for(var e=0,n=Object.values(N);e<n.length;e++){if(!n[e])return!1}return!0};return console.log("buddies",Z),(0,C.jsxs)(C.Fragment,{children:[(0,C.jsxs)(u.X2,{width:"100%",height:"73px",padding:"24px 0",alignItems:"center",justifyContent:"space-between",children:[(0,C.jsx)(u.Dx,{children:"My Buddies"}),(0,C.jsxs)(u.X2,{children:[(0,C.jsx)(g.Z,{options:[{Icon:f,text:"My Buddies",onClick:function(){e("/home/my-buddies")}},{Icon:b,text:"My transactions",onClick:function(){e("/home/transactions")}},{Icon:p,text:"Send Feedback",onClick:function(){e("/home/send/feedback")}},{Icon:j,text:"Logout",onClick:function(){n((0,x.kS)()),e("/")}}]}),(0,C.jsx)(u.hU,{onClick:function(){e("/home/notifications")},children:(0,C.jsx)(d.bI9,{})})]})]}),Boolean(F||R)?(0,C.jsx)(k.Z,{}):(0,C.jsxs)(C.Fragment,{children:[(0,C.jsxs)(u.X2,{justifyContent:"space-between",alignItems:"center",width:"100%",margin:"24px 0 12px",children:[(0,C.jsx)(u.nv,{bold:!0,fontSize:"24px",color:"#000",children:"All Buddies"}),(0,C.jsx)(u.zx,{width:"151px",height:"46px",color:"#00A652",onClick:function(){var n;"active"===(null===T||void 0===T||null===(n=T.subscription)||void 0===n?void 0:n.status)||Z.length<2?A((0,C.jsx)(l.ZB,{navigate:e,subscription:null===T||void 0===T?void 0:T.subscription,setbuddies:y,addBuddies:z,token:i,store:I})):A((0,C.jsx)(m.Z,{message:"Please Subscribe for adding more buddies \u263a\ufe0f",buttonText:"Subscribe",onSubmit:function(){e("/subscriptions")}}))},children:"+ Add new Buddy"})]}),(0,C.jsxs)(l.iA,{children:[(0,C.jsx)("thead",{children:(0,C.jsxs)(l.U8,{children:[(0,C.jsx)("th",{children:(0,C.jsx)(u.Jg,{checked:K(),onChange:function(){var e=K(),n={};Z.forEach((function(i){var t=i.id;n[t]=!e})),P(n)}})}),(0,C.jsx)("th",{children:"Contact Name"}),(0,C.jsx)("th",{children:"Relation"}),(0,C.jsx)("th",{children:"Phone Number"}),(0,C.jsx)("th",{children:"Email"}),(0,C.jsx)("th",{children:"Member Type"})]})}),(0,C.jsx)("tbody",{children:null===Z||void 0===Z?void 0:Z.map((function(e,n){return(0,C.jsxs)(l.sh,{children:[(0,C.jsx)("td",{children:(0,C.jsx)(u.Jg,{checked:!0===N[e.id],onChange:function(){return n=e.id,void P((function(e){return(0,s.Z)((0,s.Z)({},e),{},(0,t.Z)({},n,!e[n]))}));var n}})}),(0,C.jsx)("td",{children:(0,C.jsxs)(u.X2,{alignItems:"center",children:[(0,C.jsx)(u.Ee,{width:"36px",height:"36px",borderRadius:"50%",objectFit:"cover",src:"https://upload.wikimedia.org/wikipedia/commons/a/a0/Pierre-Person.jpg",alt:"Person"}),"N/A"]})}),(0,C.jsx)("td",{children:e.relationship||"N/A"}),(0,C.jsx)("td",{children:"N/A"}),(0,C.jsx)("td",{children:e.email}),(0,C.jsx)("td",{children:"N/A"}),(0,C.jsx)("td",{children:(0,C.jsx)(u.lK,{options:[{text:"Promote SubPrime",onClick:function(){}},{text:"Delete",onClick:function(){var n;n=e.id,O(n).unwrap().then().catch((function(e){console.log(e),alert(JSON.stringify(e))}))}}]})})]},n)}))})]})]})]})}}}]);
//# sourceMappingURL=625.dcfcc3cc.chunk.js.map