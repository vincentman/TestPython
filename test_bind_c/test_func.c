/*
 * test_func.c
 *
 *      Author: Vincent
 */

#include <stdio.h>
#include "test_func.h"

void test_func(struct output *out, struct input *in) {
  out->c = in->a + in->b.s;
  out->float_array[0] = in->float_array[0] + 1;
  out->float_array[1] = in->float_array[1] + 1;
  out->float_array[2] = in->float_array[2] + 1;
  out->int_array[0] = in->int_array[0] + 1;
  out->int_array[1] = in->int_array[1] + 1;
  out->int_array[2] = in->int_array[2] + 1;
  printf("[## lib ##] in.float_array[0]: %f, in.float_array[1]: %f, in.float_array[2]: %f\n",
         in->float_array[0], in->float_array[1], in->float_array[2]);
  printf("[## lib ##] in.int_array[0]: %d, in.int_array[1]: %d, in.int_array[2]: %d\n",
         in->int_array[0], in->int_array[1], in->int_array[2]);
  printf("[## lib ##] in.a: %d, in.b.s: %f, out.c: %f\n", in->a, in->b.s, out->c);
  printf("[## lib ##] out.float_array[0]: %f, out.float_array[1]: %f, out.float_array[2]: %f\n",
         out->float_array[0], out->float_array[1], out->float_array[2]);
  printf("[## lib ##] out.int_array[0]: %d, out.int_array[1]: %d, out.int_array[2]: %d\n",
         out->int_array[0], out->int_array[1], out->int_array[2]);
  fflush(stdout);
}

