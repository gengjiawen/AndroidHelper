package ${packageName};

import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import java.util.List;

import butterknife.BindView;
import butterknife.ButterKnife;

public class ${adapterClass} extends RecyclerView.Adapter {
    List<${itemClass}> ${itemClass?lower_case}List;

    @Override
    public RecyclerView.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.${adapterClass?lower_case}_item, parent, false);
        return new ${adapterClass}ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(RecyclerView.ViewHolder holder, int position) {
        ${adapterClass}ViewHolder messageViewHolder = (${adapterClass}ViewHolder) holder;
        ${itemClass} ${itemClass?lower_case} = ${itemClass?lower_case}List.get(position);
    }

    public void set${adapterClass}s(List<${itemClass}> ${itemClass?lower_case}List) {
        this.${itemClass?lower_case}List = ${itemClass?lower_case}List;
        notifyDataSetChanged();
    }

    @Override
    public int getItemCount() {
        return ${itemClass?lower_case}List == null ? 0 : ${itemClass?lower_case}List.size();
    }

    static class ${adapterClass}ViewHolder extends RecyclerView.ViewHolder {
        public ${adapterClass}ViewHolder(View view) {
            super(view);
            ButterKnife.bind(this, view);
        }
    }
}
