bl_info = {
    "name": "Simple Mesh Plugin",
    "blender": (2, 80, 0),
    "category": "Object",
}
import bpy
import bmesh
import random


def generate_terrain(width, height, scale):
    # 新しいメッシュ＆オブジェクトを制作
    mesh = bpy.data.meshes.new(name="TerrainMesh")
    obj = bpy.data.objects.new("Terrain", mesh)

    # シーンとオブジェクトをリンク
    bpy.context.collection.objects.link(obj)

    # 作ったオブジェクトを有効化
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    # エンターキーを押すとメッシュを編集モードへ
    bpy.ops.object.mode_set(mode='EDIT')

    # メッシュデータを取得
    mesh = bpy.context.edit_object.data

    # Bのメッシュオブジェクトを制作
    bm = bmesh.new()

    # テレインバーティクルを作成
    for x in range(width):
        for y in range(height):
            z = scale * random.uniform(0.0, 1.0)
            bm.verts.new(x, y, z)

    # 更新後バーティクルを同期させる
    bm.to_mesh(mesh)
    bm.free()
    # 編集モードを解除
    bpy.ops.object.mode_set(mode='OBJECT')
    # テレインをスムーズ
    bpy.ops.object.shade_smooth()

    # テレインのスケール値
    terrain_width = 50
    terrain_hight = 50
    terrain_scale = 10.0

    # テレインを作成
    generate_terrain(terrain_width, terrain_hight, terrain_scale)
