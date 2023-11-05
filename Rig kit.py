import maya.cmds as cmds
def controlatworld():
    
    import maya.cmds as cmds
    sel=cmds.ls(sl=1,fl=1)
    for each in sel:
        pos=cmds.xform(each,q=True,ws=1,t=1)
        cmds.select(cl=1)
        ctrl=cmds.circle(ch=0)
        grp=cmds.group()
        jnt=cmds.joint()
        cmds.parent(jnt,ctrl)
        cmds.xform(grp,t=pos)
        #ctrlpos
      
def controlatlocal():
    
    import maya.cmds as cmds
    sel=cmds.ls(sl=1,fl=1)
    for each in sel:
        pos=cmds.xform(each,q=True,ws=1,t=1)
        cmds.select(cl=1)
        ctrl=cmds.circle(ch=0)
        grp=cmds.group()
        jnt=cmds.joint()
        cmds.parent(jnt,ctrl)
        cmds.select(each)
        xyz=cmds.pointOnPolyConstraint(each,grp,mo=0)
        print(each)
        cmds.delete(xyz)
        cmds.xform(grp,t=pos)
        #ctrlpos
        
def follicleatpivot():
    
    import maya.cmds as cmds
    sel=cmds.ls(sl=1,fl=1)
    for each in sel:
        pos=cmds.xform(each,q=True,ws=1,t=1)
        cmds.select(cl=1)
        np=cmds.nurbsPlane(ch=0)
        abc=cmds.listRelatives(np,s=True)[0]
        #grp=cmds.group()
        fol=cmds.createNode('follicle')
        cmds.select(each)
        xyz=cmds.listRelatives(fol,p=True)[0]
        cmds.xform(np,t=pos)
        cmds.xform(xyz,t=pos)
        
        #cmds.parent(xyz,grp)
        cmds.connectAttr(fol+".outTranslate",xyz+".translate")
        cmds.connectAttr(fol+".outRotate",xyz+".rotate")
        cmds.connectAttr(abc+".local",xyz+".inputSurface")
        cmds.connectAttr(abc+".worldMatrix[0]",xyz+".inputWorldMatrix")
        cmds.setAttr(fol+".parameterV" ,0.5)
        cmds.setAttr(fol+".parameterU" ,0.5)
        #create a group and parent the all object
        grp=cmds.group(xyz,np)
    
    
    
             
   
        
    
    
      
       
    





def customwindow(name):
    
    if cmds.window(name,exists=1):
        cmds.deleteUI(name)
    mywindow=cmds.window(name,width=350,height=700,sizeable=1)
    cmds.showWindow(mywindow)
    ############################
    wWidth=350
    wHeight=400
    
    
    
    cmds.columnLayout()
    cmds.button(label="Create Control at Each Vertex(World)",c="controlatworld()",width=wWidth,height=133,bgc=(0,0.2,0.2))
    cmds.button(label="Create Control at Each Vertex(Local)",c="controlatlocal()",width=wWidth,height=133,bgc=(0,0.2,0.2))
    cmds.button(label="Create Follicle at Each Pivot",c="follicleatpivot()",width=wWidth,height=133,bgc=(0,0.2,0.2)) 
    cmds.setParent("..")
    
    cmds.columnLayout()
    
   
    
    cmds.setParent("..")
    
    
    
customwindow("RiggingKit_V1.0 - Augustina ")
