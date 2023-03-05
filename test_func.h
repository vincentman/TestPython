/*
 * tmpProject.h
 *
 *  Created on: 2023
 *      Author: Vincent
 */

#ifndef TEST_FUNC_H_
#define TEST_FUNC_H_

struct simple {
  int s;
};

struct input {
  int a;
  struct simple b;
};

struct output {
  int c;
};

void test_func(struct output *out, struct input *in);

#endif /* TEST_FUNC_H_ */
