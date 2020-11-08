// import Model from '@ember-data/model';
// export default class BookModel extends Model {}

import DS from 'ember-data';
export default DS.Model.extend({
    title: DS.attr(),
    author: DS.attr(),
    description: DS.attr()
})