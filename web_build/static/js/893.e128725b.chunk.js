"use strict";(self.webpackChunkweb=self.webpackChunkweb||[]).push([[893],{5893:function(n,e,A){A.r(e),A.d(e,{default:function(){return X}});var t=A(5861),r=A(885),o=A(4687),i=A.n(o),s=A(2791),d=A(71),u=A(6871),l=A(8529),c=A(9970),f=A(629),a=A(1484),g=A(144),w=A(9478),C=A(7820),x=A(2978),p=A(8609),b=A(4554),v=A(8852),h=A(7201),B=A(9696),m=A(7394),Q=A(184);function X(){var n=(0,u.s0)(),e=(0,x.I0)(),A=(0,u.UO)(),o=(0,s.useRef)(null),X=(0,B.j3)(),W=(0,r.Z)(X,2),Z=W[0],j=W[1].isLoading,y=(0,B.g3)(),L=(0,r.Z)(y,1)[0],U=(0,B.cQ)(A.id),z=U.data,F=U.isLoading,H=U.isSuccess,P=U.error;if(console.log("files of folder...",z,F,H,P),F)return null;var G=function(){var n=(0,t.Z)(i().mark((function n(e){return i().wrap((function(n){for(;;)switch(n.prev=n.next){case 0:console.log("file to copy",e);case 1:case"end":return n.stop()}}),n)})));return function(e){return n.apply(this,arguments)}}();return(0,Q.jsxs)(Q.Fragment,{children:[(0,Q.jsxs)(l.X2,{width:"100%",height:"73px",padding:"24px 0",alignItems:"center",justifyContent:"space-between",children:[(0,Q.jsx)(p.Z,{}),(0,Q.jsxs)(l.Dx,{margin:"0px 0px 0px 80px",children:["Folders ",">"," ",z.name]}),(0,Q.jsxs)(l.X2,{children:[(0,Q.jsx)(C.Z,{options:[{Icon:f,text:"My Buddies",onClick:function(){n("/home/my-buddies")}},{Icon:g,text:"My transactions",onClick:function(){n("/home/transactions")}},{Icon:w,text:"Send Feedback",onClick:function(){n("/home/send/feedback")}},{Icon:a,text:"Logout",onClick:function(){e((0,c.kS)()),n("/")}}]}),(0,Q.jsx)(l.hU,{onClick:function(){n("/home/notifications")},children:(0,Q.jsx)(d.bI9,{})})]})]}),(0,Q.jsxs)("div",{style:{display:"flex",flexDirection:"row",alignItems:"flex-start"},children:[(0,Q.jsxs)(b.Z,{width:"85%",height:"auto",sx:{display:"flex",flexWrap:"wrap"},children:[Boolean(z.files.length)&&z.files.map((function(n,e){return(0,Q.jsxs)(v.Z,{width:"150px",height:"150px",flexDirection:"column",justifyContent:"flex-start",alignItems:"flex-start",padding:"10px",margin:"10px",borderRadius:"15px",children:[(0,Q.jsx)("div",{style:{width:"100%",display:"flex",justifyContent:"flex-end"},children:(0,Q.jsx)(l.lK,{color:"rgba(0, 0, 0, 0.4)",orientation:"horizontal",options:[{text:"Open",onClick:function(){window.open(n.file)}},{text:"Rename",onClick:function(){}},{text:"Delete",onClick:function(){L(n.id)}},{text:"Make a Copy",onClick:function(){G(n)}}]})}),(0,Q.jsx)(l.sg,{justifyContent:"flex-end",children:(0,Q.jsxs)(l.X2,{alignItems:"center",margin:"0px 0px 15px",children:[n.extension.includes("application")?(0,Q.jsx)(d.jyt,{color:"#00A652",size:"18px"}):n.extension.includes("image")?(0,Q.jsx)(d.tpQ,{color:"#FF5F5F",size:"18px"}):n.extension.includes("music")?(0,Q.jsx)(d.A7v,{color:"#1877F2",size:"18px"}):(0,Q.jsx)(d.UuI,{color:"#00A652",size:"18px"}),(0,Q.jsx)(l.Dx,{fontSize:"10px",margin:"0px 10px",children:(0,h.a)(n.name)})]})})]},e)})),j?(0,Q.jsx)(D,{}):(0,Q.jsx)(Q.Fragment,{children:!Boolean(z.files.length)&&(0,Q.jsxs)("div",{style:{display:"flex",flex:1,flexDirection:"column",alignItems:"center",justifyContent:"center",width:"100%",height:"80vh"},children:[(0,Q.jsx)("img",{src:"data:image/png;base64,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",height:"240px",width:"240px"}),(0,Q.jsx)(l.nv,{margin:"10px 0px",children:"Drop files here"})]})})]}),(0,Q.jsx)(b.Z,{width:"15%",children:(0,Q.jsxs)(m.RV,{onClick:function(){return o.current.click()},position:"static",width:"100%",children:["+ Upload new File",(0,Q.jsx)("input",{type:"file",onClick:function(n){n.target.value=null},onChange:function(n){Z({file:n.target.files[0],folderId:z.id}).unwrap().then((function(n){return console.log("upload file",n)}))},ref:o,style:{display:"none"}})]})})]})]})}var D=function(){return(0,Q.jsx)(v.Z,{width:"150px",height:"150px",flexDirection:"column",justifyContent:"center",alignItems:"center",padding:"10px",margin:"10px",borderRadius:"15px",children:(0,Q.jsxs)("div",{style:{display:"flex",alignItems:"center"},children:[(0,Q.jsx)(d.UuI,{color:"#00A652",size:"18px"}),(0,Q.jsx)(l.Dx,{fontSize:"12px",margin:"0px 10px",children:"Uploading..."})]})})}},8609:function(n,e,A){A.d(e,{Z:function(){return l}});var t,r=A(168),o=(A(2791),A(7691)),i=A(6856),s=A(6871),d=A(184),u=o.ZP.div(t||(t=(0,r.Z)(['\n  width: 64px;\n  height: 55px;\n  font-family: "TT Commons";\n  font-style: normal;\n  display: flex;\n  justify-content: center;\n  align-items: flex-start;\n  position: ',";\n  ","\n  border-radius: 10px;\n  cursor: pointer;\n  font-weight: ",";\n"])),(function(n){var e;return null!==(e=n.position)&&void 0!==e?e:"absolute"}),(function(n){return n.position&&"\n  top: 50px;\n  left: 250px;\n  "}),(function(n){var e;return null!==(e=n.fontWeight)&&void 0!==e?e:"600"}));function l(){var n=(0,s.s0)();return(0,d.jsx)(u,{onClick:function(){return n(-1)},children:(0,d.jsx)(i.dWm,{style:{marginTop:15},size:25})})}},4554:function(n,e,A){A.d(e,{Z:function(){return w}});var t=A(7462),r=A(3366),o=A(2791),i=A(8182),s=A(3842),d=A(104),u=A(8519),l=A(886),c=A(184),f=["className","component"];var a=A(5902),g=function(){var n=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},e=n.defaultTheme,A=n.defaultClassName,a=void 0===A?"MuiBox-root":A,g=n.generateClassName,w=n.styleFunctionSx,C=void 0===w?d.Z:w,x=(0,s.ZP)("div",{shouldForwardProp:function(n){return"theme"!==n&&"sx"!==n&&"as"!==n}})(C),p=o.forwardRef((function(n,A){var o=(0,l.Z)(e),s=(0,u.Z)(n),d=s.className,w=s.component,C=void 0===w?"div":w,p=(0,r.Z)(s,f);return(0,c.jsx)(x,(0,t.Z)({as:C,ref:A,className:(0,i.Z)(d,g?g(a):a),theme:o},p))}));return p}({defaultTheme:(0,A(3771).Z)(),defaultClassName:"MuiBox-root",generateClassName:a.Z.generate}),w=g}}]);
//# sourceMappingURL=893.e128725b.chunk.js.map