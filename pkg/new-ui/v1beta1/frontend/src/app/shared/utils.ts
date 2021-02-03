import lowerCase from 'lodash-es/lowerCase';
import { ParameterSpec } from '../shared/params-list/types';
import { FormControl, FormGroup, Validators, FormArray } from '@angular/forms';
import { NasOperation } from '../pages/experiment-creation/nas-operations/types';

export function createNasOperationGroup(op: NasOperation): FormGroup {
  const array = op.params.map(param => createParameterGroup(param));

  return new FormGroup({
    type: new FormControl(op.type, Validators.required),
    params: new FormArray(array),
  });
}

export function createParameterGroup(param: ParameterSpec): FormGroup {
  const paramForm = new FormGroup({
    name: new FormControl(param.name, Validators.required),
    type: new FormControl(param.type, Validators.required),
  });

  if (Array.isArray(param.value)) {
    const ctrls = param.value.map(v => new FormControl(v, Validators.required));
    paramForm.addControl('value', new FormArray(ctrls, Validators.required));
    return paramForm;
  }

  paramForm.addControl(
    'value',
    new FormGroup({
      min: new FormControl(param.value.min, Validators.required),
      max: new FormControl(param.value.max, Validators.required),
      step: new FormControl(param.value.step, []),
    }),
  );

  return paramForm;
}

/*
 * Arithmetics
 **/
export const numberToExponential = (num: number, digits: number): string => {
  if (isNaN(Number(num))) {
    return '';
  }

  if (num.toString().replace(/[.]/g, '').length <= digits) {
    return num.toString();
  }

  if (
    num.toExponential().search(/e[+]1/) > -1 ||
    num.toExponential().search(/e[-]1/) > -1
  ) {
    const slicedNumber = num.toString().slice(0, digits + 1);

    return slicedNumber.replace(/[.]*0+$/, '');
  }

  let exponentialNumber = num.toExponential(digits - 1);

  // If toExponential added e+0 in the end of the string remove it
  exponentialNumber = exponentialNumber.replace(/[.]*0*e[+]0$/, '');

  // If the number is e.g. 2.1000e-3, the zeros must to be removed
  if (/[.]*0+e[+-][1-9]$/.test(exponentialNumber)) {
    // Split the number and the exponent in order to remove from
    // the number the zeros
    const [numberToFix, exponentNumber] = exponentialNumber.split('e');
    const fixed = numberToFix.replace(/[0]*$/g, '');

    // Build again the exponential number
    exponentialNumber = `${fixed}e${exponentNumber}`;

    /*If the number was e.g. 2.000e-3 after the above replacement
    it would be 2.e-3 so a zero between . and e has to be added*/
    return exponentialNumber.replace(/[.]e/g, '.0e');
  }

  return exponentialNumber;
};

export const transformStringResponses = (
  response: string,
): { types: string[]; details: string[][] } => {
  response = response.replace(/\n$/, '');

  // Separate each line
  const lines = response.split('\n');
  let types = [];
  let details = [];

  // The first line is the names of the types
  types = lines[0].split(',');
  // Transform them for consistency
  types = types.map(column => lowerCase(column));

  // Separate types from details of every item
  lines.splice(0, 1);

  // Change the first letter of the column to upper case
  types = types.map(column => column.charAt(0).toUpperCase() + column.slice(1));

  // Transform the details of each item from string to an array
  details = lines.map(detail => detail.split(','));

  return { types, details };
};

export const safeDivision = (divided: number, divider: number): number =>
  Math.round((divided * 10000.0) / divider) / 10000;

export const safeMultiplication = (
  multiplicand: number,
  multiplier: number,
): number => Math.round(multiplicand * 10000.0 * multiplier) / 10000;
