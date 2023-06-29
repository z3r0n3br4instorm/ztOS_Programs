import pyopencl as cl
import numpy as np
import time

def run_gpu():
    # Set up OpenCL context and queue
    platform = cl.get_platforms()[0]
    device = platform.get_devices(device_type=cl.device_type.GPU)[0]
    context = cl.Context([device])
    queue = cl.CommandQueue(context)

    # Create input and output buffers
    input_data = np.array([1, 2, 3, 4, 5], dtype=np.float32)
    output_data = np.zeros_like(input_data)
    input_buffer = cl.Buffer(context, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=input_data)
    output_buffer = cl.Buffer(context, cl.mem_flags.WRITE_ONLY, size=output_data.nbytes)

    # Build the OpenCL program
    source_code = """
    __kernel void square(__global const float* input, __global float* output) {
        int i = get_global_id(0);
        output[i] = input[i] * input[i];
    }
    """
    program = cl.Program(context, source_code).build()

    # Set kernel arguments and enqueue the kernel for execution
    program.square(queue, input_data.shape, None, input_buffer, output_buffer)

    # Read back the results from the output buffer
    cl.enqueue_copy(queue, output_data, output_buffer)

    return output_data

def run_cpu():
    # Create input data
    input_data = np.array([1, 2, 3, 4, 5], dtype=np.float32)

    # Compute the result on the CPU
    output_data = np.square(input_data)

    return output_data

# Run GPU computation
start_time = time.time()
gpu_output = run_gpu()
gpu_execution_time = time.time() - start_time

# Run CPU computation
start_time = time.time()
cpu_output = run_cpu()
cpu_execution_time = time.time() - start_time

# Print the results
print("GPU Output:", gpu_output)
print("CPU Output:", cpu_output)
print("GPU Execution Time:", gpu_execution_time)
print("CPU Execution Time:", cpu_execution_time)