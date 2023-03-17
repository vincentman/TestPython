/*
 * tmpProject.h
 *
 *  Created on: 2023
 *      Author: Vincent
 */

#ifndef TEST_FUNC_H_
#define TEST_FUNC_H_

struct simple {
  float s;
  float s2;  // not used
};

struct input {
  int a;
  struct simple b;
  struct simple b2; // not used
  float float_array[3];
  int int_array[3];
};

struct output {
  float c;
  float float_array[3];
  int int_array[3];
};

void test_func(struct output *out, struct input *in);

#endif /* TEST_FUNC_H_ */
