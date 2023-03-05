/*
 * test_func.c
 *
 *      Author: Vincent
 */

#include "test_func.h"

void test_func(struct output *out, struct input *in) {
  out->c = in->a + in->b.s;
}



