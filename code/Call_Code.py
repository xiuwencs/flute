import random
import subprocess
import os
def Diffu_Edge(pathout, output_file):
    # 利用bash调用DiffusionEdge算法，进行图像边缘检测
    path = pathout + output_file
    input_dir = "../result/" + output_file+"/Original_image_file"
    out_dir = "../result/" + output_file+"/Edterout_file"
    bash_script = f"""
    #!/bin/bash

    # Initialize conda
    source ~/anaconda3/etc/profile.d/conda.sh  # Adjust this path if needed

    conda init
    # Activate the conda environment
    conda activate diffedge
    conda info --envs
    cd DiffusionEdge
    
    # Run the Python script with input_dir and out_dir as arguments
    python demo.py --input_dir {input_dir} --pre_weight nyud.pt --out_dir {out_dir} --bs 32

    # Return conda
    conda activate code

    echo "已完成图像处理"

    """
    bash_file_path = os.path.join(path, output_file + "_run_diffedge.sh")
    # 检查文件是否存在
    if os.path.isfile(bash_file_path):
        # 如果文件存在，则删除它
        try:
            os.remove(bash_file_path)
#            print(f"已删除文件: {bash_file_path}")
        except OSError as e:
            # 如果删除文件时发生错误（比如权限问题），则打印错误信息
            print(f"无法删除文件: {bash_file_path}. 错误: {e.strerror}")

    bash_file_path = os.path.join(path, output_file + "_run_diffedge.sh")
    with open(bash_file_path, "w") as f:
        f.write(bash_script)

    # Make the script executable
    os.chmod(bash_file_path, 0o755)
#    print(bash_file_path)

    # Execute the bash script
#    os.system(f"{bash_file_path}")
    result = subprocess.run(['bash', bash_file_path], capture_output=True)

def Netplier_result(pic_num, pathout, output_file):
    path = pathout + output_file
    input_dir = "result/" + output_file + "/slip_pcapng_file"
    out_dir = "result/" + output_file + "/netplier_file"
    # 生成1到30之间的随机整数（包括1和30）
    random_number = random.randint(1, pic_num)
    input_dir = input_dir + "/" + str(random_number) + ".pcapng"
    bash_script = f"""
    #!/bin/bash

    # Initialize conda
    source ~/anaconda3/etc/profile.d/conda.sh  # Adjust this path if needed
    conda init
    conda info --envs

    # Activate the conda environment
    conda activate netplier


    # Run the Python script with input_dir and out_dir as arguments
    python3 NetPlier-master/netplier/main.py -i {input_dir} -o {out_dir}

    # Return conda
    conda activate code

    """
    bash_file_path = os.path.join(path, output_file + "_run_netplier.sh")
    # 检查文件是否存在
    if os.path.isfile(bash_file_path):
        # 如果文件存在，则删除它
        try:
            os.remove(bash_file_path)
#            print(f"已删除文件: {bash_file_path}")
        except OSError as e:
            # 如果删除文件时发生错误（比如权限问题），则打印错误信息
            print(f"无法删除文件: {bash_file_path}. 错误: {e.strerror}")
    
    bash_file_path = os.path.join(path, output_file + "_run_netplier.sh")
    with open(bash_file_path, "w") as f:
        f.write(bash_script)

    # Make the script executable
    os.chmod(bash_file_path, 0o755)

    # Execute the bash script
    subprocess.run(['bash', bash_file_path], capture_output=True, text=True)
    return 0
 
if __name__ == '__main__':
    Diffu_Edge("result/","dhcp")