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
    
