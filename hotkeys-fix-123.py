bl_info = {
    "name": "Hotkeys Fix 123",
    "blender": (4, 0, 0),
    "version": (1,0),
    "category": "Object",
    "description": "Enter 1,2,3 to vertex, edge, face from Object Mode",
    "author": "abhiraaid",
}

import bpy

class VertexMode(bpy.types.Operator):
    bl_idname = "object.vertex_mode"
    bl_label = "Vertex Mode"
    
    def execute(self, context):
        if bpy.context.mode == 'OBJECT':
            selected_meshes = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
            if selected_meshes:
                bpy.context.view_layer.objects.active = selected_meshes[0]
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_mode(type='VERT')
        return {'FINISHED'}

class EdgeMode(bpy.types.Operator):
    bl_idname = "object.edge_mode"
    bl_label = "Edge Mode"

    def execute(self, context):
        if bpy.context.mode == 'OBJECT':
            selected_meshes = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
            if selected_meshes:
                bpy.context.view_layer.objects.active = selected_meshes[0]
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_mode(type='EDGE')
        return {'FINISHED'}

class FaceMode(bpy.types.Operator):
    bl_idname = "object.face_mode"
    bl_label = "Face Mode"

    def execute(self, context):
        if bpy.context.mode == 'OBJECT':
            selected_meshes = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
            if selected_meshes:
                bpy.context.view_layer.objects.active = selected_meshes[0]
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_mode(type='FACE')
        return {'FINISHED'}
           

def menu_func(self, context):
    layout = self.layout
    layout.operator("object.vertex_mode")
    layout.operator("object.edge_mode")
    layout.operator("object.face_mode")

def register():
    bpy.utils.register_class(VertexMode)
    bpy.utils.register_class(EdgeMode)
    bpy.utils.register_class(FaceMode)
    
    # Define the keymap items
    wm = bpy.context.window_manager
    
    # Vertex Mode (Hotkey: 1)
    km = wm.keyconfigs.addon.keymaps.new(name="Object Mode")
    kmi = km.keymap_items.new("object.vertex_mode", type='ONE', value='PRESS')
    kmi.active = True
    
    # Edge Mode (Hotkey: 2)
    kmi = km.keymap_items.new("object.edge_mode", type='TWO', value='PRESS')
    kmi.active = True
    
    # Face Mode (Hotkey: 3)
    kmi = km.keymap_items.new("object.face_mode", type='THREE', value='PRESS')
    kmi.active = True
    
   

def unregister():
    bpy.utils.unregister_class(VertexMode)
    bpy.utils.unregister_class(EdgeMode)
    bpy.utils.unregister_class(FaceMode)

if __name__ == "__main__":
    register()

